from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import requests
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os
from flaskwebgui import FlaskUI

# Determine the absolute path to the directory containing this script
# This ensures PyInstaller can find index.html after bundling
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
CORS(app)

def fetch_usgs_wms(lat, lon, scale_km):
    """Fetches the base elevation image from USGS."""
    deg_span = scale_km / 30.32
    min_lon, max_lon = (lon % 360) - (deg_span / 2), (lon % 360) + (deg_span / 2)
    min_lat, max_lat = lat - (deg_span / 2), lat + (deg_span / 2)
    
    wms_url = "https://planetarymaps.usgs.gov/cgi-bin/mapserv"
    params = {
        "map": "/maps/earth/moon_simp_cyl.map",
        "service": "WMS",
        "request": "GetMap",
        "version": "1.1.1",
        "layers": "LOLA_steel",
        "styles": "",
        "srs": "EPSG:4326",
        "bbox": f"{min_lon},{min_lat},{max_lon},{max_lat}",
        "width": "600",
        "height": "600",
        "format": "image/png"
    }
    
    response = requests.get(wms_url, params=params)
    if response.status_code != 200 or b"ServiceExceptionReport" in response.content[:200]:
        raise Exception("USGS MapServer error. Check your coordinates.")
        
    return Image.open(BytesIO(response.content)).convert('L')

# NEW: Route to serve the frontend interface
@app.route('/')
def index():
    html_path = os.path.join(BASE_DIR, 'index.html')
    return send_file(html_path)

@app.route('/calculate-settlement', methods=['GET'])
def calculate_settlement():
    try:
        lat = float(request.args.get('lat', 0))
        lon = float(request.args.get('lon', 0))
        scale = float(request.args.get('scale', 100))
        
        w_flat = float(request.args.get('w_flat', 0.5))
        w_elev = float(request.args.get('w_elev', 0.5))
        
        total_weight = w_flat + w_elev
        if total_weight > 0:
            w_flat /= total_weight
            w_elev /= total_weight
        else:
            w_flat, w_elev = 0.5, 0.5

        deg_span = scale / 30.32

        img = fetch_usgs_wms(lat, lon, scale)
        elev_matrix = np.array(img, dtype=float)
        elev_norm = elev_matrix / 255.0
        
        gy, gx = np.gradient(elev_matrix)
        lat_rows = np.linspace(lat + deg_span/2, lat - deg_span/2, 600)
        cos_lat = np.clip(np.cos(np.radians(lat_rows)), 0.01, 1.0)
        cos_matrix = np.tile(cos_lat[:, np.newaxis], (1, 600))
        
        gx_corrected = gx / cos_matrix
        slope_matrix = np.sqrt(gx_corrected**2 + gy**2)
        slope_norm = np.clip(slope_matrix / 20.0, 0.0, 1.0)
        flatness_matrix = 1.0 - slope_norm
        
        suitability_score = (flatness_matrix * w_flat) + (elev_norm * w_elev)
        
        lon_normalized = (lon + 180) % 360 - 180
        comm_score = max(0.0, float(np.cos(np.radians(lon_normalized))))
        comm_percent = round(comm_score * 100)
        
        if comm_percent > 75:
            comm_status = "Excellent (Direct Line of Sight)"
        elif comm_percent > 15:
            comm_status = "Marginal (Low Horizon Window)"
        else:
            comm_percent = 0
            comm_status = "No Signal (Far Side Shadow Zone)"
        
        cmap = plt.get_cmap('RdYlGn')
        heatmap_img_array = cmap(suitability_score)
        heatmap_img = Image.fromarray((heatmap_img_array[:, :, :3] * 255).astype(np.uint8))
        
        heatmap_io = BytesIO()
        heatmap_img.save(heatmap_io, format='PNG')
        heatmap_b64 = base64.b64encode(heatmap_io.getvalue()).decode('utf-8')
        
        orig_io = BytesIO()
        img.save(orig_io, format='PNG')
        orig_b64 = base64.b64encode(orig_io.getvalue()).decode('utf-8')
        
        return jsonify({
            "original": f"data:image/png;base64,{orig_b64}",
            "heatmap": f"data:image/png;base64,{heatmap_b64}",
            "comm_percent": comm_percent,
            "comm_status": comm_status
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # NEW: Launch as a desktop application instead of a background server
    FlaskUI(app=app, server="flask", port=5000, width=1200, height=800).run()