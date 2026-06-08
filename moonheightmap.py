from flask import Flask, request, send_file, jsonify
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/get-lunar-map', methods=['GET'])
def get_lunar_map():
    try:
        # Pull parameters dynamically from the web URL query string
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon')) % 360
        scale_km = float(request.args.get('scale', 100))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing parameters"}), 400

    # Bounding Box Logic
    deg_span = scale_km / 30.32
    wms_url = "https://planetarymaps.usgs.gov/cgi-bin/mapserv"
    
    params = {
        "map": "/maps/earth/moon_simp_cyl.map",
        "service": "WMS",
        "request": "GetMap",
        "version": "1.1.1",
        "layers": "LOLA_color",
        "styles": "",
        "srs": "EPSG:4326",
        "bbox": f"{lon - deg_span/2},{lat - deg_span/2},{lon + deg_span/2},{lat + deg_span/2}",
        "width": "800",
        "height": "800",
        "format": "image/png"
    }

    response = requests.get(wms_url, params=params)
    
    if response.status_code == 200 and response.headers.get('Content-Type', '').startswith('image/'):
        # Stream the image file bytes directly into the user's web browser
        return send_file(BytesIO(response.content), mimetype='image/png')
    else:
        return jsonify({"error": "USGS Server error or invalid coordinates structure"}), 502

if __name__ == '__main__':
    # Runs a local server at http://127.0.0.1:5000
    app.run(debug=True)