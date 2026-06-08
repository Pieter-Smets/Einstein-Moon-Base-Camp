# Einstein Moon Base Camp 🌙

A comprehensive interactive dashboard for lunar habitat simulation and analysis. This educational platform provides tools for understanding the physics, biology, and geography required for establishing a sustainable human presence on the Moon.

**Live Demo:** [Einstein Moon Base Camp](https://pieter-smets.github.io/Einstein-Moon-Base-Camp/)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
  - [Algen Bioreactor](#1-algen-bioreactor)
  - [Catapult Trajectory Simulation](#2-catapult-trajectory-simulation)
  - [Centrifuge Simulator](#3-centrifuge-simulator)
  - [Lunar Map Explorer](#4-lunar-map-explorer)
  - [Lunar Settlement Suitability (GIS)](#5-lunar-settlement-suitability-gis)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [License](#license)

---

## Overview

Einstein Moon Base Camp is an interactive educational platform designed to explore the multifaceted challenges of establishing a lunar habitat. Students and researchers can simulate critical systems including:

- **Life Support:** Oxygen generation through algae-based bioreactors
- **Transportation:** Catapult-based payload delivery systems
- **Artificial Gravity:** Centrifuge design for crew health maintenance
- **Geography & Terrain:** Interactive lunar topography exploration
- **Site Selection:** GIS-based analysis for optimal settlement locations

The platform emphasizes hands-on learning through interactive simulations with real-world parameters and USGS lunar data.

---

## Features

### 1. **Algen Bioreactor** 🌿
*Module: `Algen.html`*

Calculate the oxygen production capacity required to sustain a lunar habitat crew.

**Functionality:**
- Input parameters: crew size, oxygen consumption rate, algae concentration, and production factors
- Real-time calculations of:
  - Total daily oxygen demand per crew
  - Required water volume for bioreactor
  - Algae biomass needed
  - Production efficiency metrics
- Detailed output showing system feasibility and sustainability ratios

**Educational Goals:**
- Understand biological life support systems
- Explore photosynthetic oxygen production
- Calculate resource requirements for human survival
- Analyze bioreactor efficiency metrics

**Key Parameters:**
- Oxygen consumption: ~0.84 kg/person/day (reference: average human consumption)
- Algae concentration: adjustable (kg/liter)
- Production factor: growth rate multiplier

---

### 2. **Catapult Trajectory Simulation** 🚀
*Module: `CatapultSimulation.html`*

Simulate ballistic trajectories for lunar payload delivery systems under variable gravity.

**Functionality:**
- Input parameters: object mass, initial velocity, launch angle, gravity level
- Real-time trajectory calculations including:
  - Maximum height reached
  - Total flight time
  - Horizontal range
  - Impact velocity
  - Kinetic energy at launch and impact
- Visual graph plotting trajectory path
- Spreadsheet-style data export with trajectory points

**Educational Goals:**
- Apply kinematics and projectile motion physics
- Understand gravity effects on trajectories
- Optimize launch parameters for cargo delivery
- Explore energy conservation principles

**Key Parameters:**
- Moon gravity: -1.62 m/s² (approximately 1/6th of Earth's)
- Adjustable launch angles: 0-90°
- Customizable initial velocities and object masses

**Physics Formulas Used:**
- Horizontal position: $x(t) = v_0 \cos(\theta) \cdot t$
- Vertical position: $y(t) = v_0 \sin(\theta) \cdot t + \frac{1}{2}g t^2$
- Range: $R = \frac{v_0^2 \sin(2\theta)}{|g|}$
- Maximum height: $h_{max} = \frac{(v_0 \sin(\theta))^2}{2|g|}$

---

### 3. **Centrifuge Simulator** 🔄
*Module: `centrifuge.html`*

Design and analyze rotating centrifuges for generating artificial gravity.

**Functionality:**
- Input parameters: radius, desired gravity level, object mass
- Real-time calculations of:
  - Required angular velocity (rad/s and RPM)
  - Rotation frequency and period
  - Centripetal acceleration
  - Centripetal force required
  - Required tension/structural support
- Interactive parameter adjustment
- Real-time output updates

**Educational Goals:**
- Understand circular motion physics
- Explore artificial gravity generation
- Analyze structural requirements for rotating habitats
- Study centripetal force and acceleration

**Key Parameters:**
- Radius: distance from rotation axis (meters)
- Target gravity: desired acceleration (m/s²)
- Mass: test object or crew member mass

**Physics Formulas Used:**
- Centripetal acceleration: $a_c = \omega^2 r = \frac{v^2}{r}$
- Angular velocity: $\omega = \sqrt{\frac{a_c}{r}}$
- Centripetal force: $F_c = m \omega^2 r$
- Frequency: $f = \frac{\omega}{2\pi}$
- Period: $T = \frac{1}{f} = \frac{2\pi}{\omega}$

---

### 4. **Lunar Map Explorer** 🌑
*Module: `MoonMap.html`*

Interactive exploration of lunar topography using NASA LRO/LOLA elevation data.

**Functionality:**
- Interactive web-based map powered by Leaflet.js
- USGS WMS integration for real-time lunar terrain data
- Pan and zoom controls for detailed exploration
- LOLA (Lunar Orbiter Laser Altimeter) elevation data visualization
- High-resolution topographic color mapping

**Data Source:**
- **USGS Planetary Maps**: Official NASA/USGS lunar cartography
- **LOLA Data**: Comprehensive lunar elevation mapping with meter-scale resolution
- **WMS Service**: Web Map Service for dynamic tile generation

**Educational Goals:**
- Visualize lunar terrain and topography
- Identify terrain features and geological formations
- Explore potential settlement sites
- Understand elevation variations across lunar surface

**Technical Details:**
- Map tiles generated via USGS WMS service
- Leaflet.js for interactive mapping interface
- Support for standard web mercator and lunar projections

---

### 5. **Lunar Settlement Suitability (GIS)** 📍
*Module: `Habitability.html`*

Geographic Information System (GIS) analysis for optimal lunar settlement site selection.

**Functionality:**
- Interactive slider controls for filtering parameters:
  - Elevation range
  - Solar illumination percentage
  - Temperature constraints
  - Slope angle limitations
  - Water ice proximity
- Real-time map updates showing suitable locations
- Color-coded suitability visualization
- Location coordinate display
- Parameter-based filtering for multi-criteria analysis

**Educational Goals:**
- Understand GIS and spatial analysis
- Learn multi-criteria decision analysis
- Identify optimal settlement locations based on constraints
- Explore trade-offs between different environmental factors

**Key Selection Criteria:**
- **Elevation**: Affects atmospheric pressure, resource accessibility
- **Solar Access**: Influences power generation (solar panels)
- **Temperature**: Affects equipment operation and crew safety
- **Slope**: Determines construction difficulty and stability
- **Water Ice**: Critical resource for habitat sustainability

---

## Project Structure

```
Einstein Moon Base Camp/
├── index.html                 # Main dashboard/landing page
├── Algen.html                 # Algae bioreactor simulator
├── CatapultSimulation.html    # Ballistic trajectory simulator
├── centrifuge.html            # Centrifuge/artificial gravity simulator
├── MoonMap.html               # Interactive lunar map viewer
├── Habitability.html          # GIS-based site selection tool
├── moonheightmap.py           # Flask backend for USGS map tiles
├── style.css                  # Global CSS styling
└── README.md                  # This file
```

---

## Technology Stack

### Frontend
- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with CSS variables and media queries
- **JavaScript**: Interactive simulations and calculations
- **Leaflet.js**: Interactive mapping library (v1.9.4)

### Backend (Optional)
- **Flask**: Python microframework for WMS proxy service
- **USGS WMS Service**: NASA lunar cartography data source
- **Requests Library**: HTTP client for external API calls

### Data Sources
- **USGS Planetary Maps**: Official lunar elevation and imagery data
- **LOLA (Lunar Orbiter Laser Altimeter)**: High-resolution elevation dataset
- **NASA LRO (Lunar Reconnaissance Orbiter)**: Orbital imagery and measurements

### Design & UX
- **Responsive Design**: Mobile-first approach with media queries
- **Accessibility**: Semantic HTML and keyboard navigation support
- **CSS Custom Properties**: Theme-based color system for consistency
- **Modern UI Patterns**: Cards, buttons, input groups, and layouts

---

## Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection (for WMS tile loading and external resources)
- Optional: Python 3.6+ and Flask (for local WMS proxy)

### Quick Start

1. **Access Online:**
   Simply visit the [live demo](https://pieter-smets.github.io/Einstein-Moon-Base-Camp/)

2. **Local Setup:**
   - Clone or download the repository
   - Open `index.html` in your web browser
   - Navigate through modules using the dashboard menu

---

## Installation & Setup

### Option 1: Static Hosting (Recommended)

```bash
# Clone the repository
git clone https://github.com/Pieter-Smets/Einstein-Moon-Base-Camp.git
cd Einstein-Moon-Base-Camp

# Open index.html in your browser
# On Windows:
start index.html

# On macOS:
open index.html

# On Linux:
xdg-open index.html
```

### Option 2: Local Python Server (with WMS Proxy)

```bash
# Install dependencies
pip install flask requests

# Run the Flask server
python moonheightmap.py

# Server runs at http://localhost:5000
# Access through a local HTTP server for the main site:
# Python 3
python -m http.server 8000

# Then visit http://localhost:8000 in your browser
```

### Option 3: Docker

```bash
# Create a Dockerfile (if needed for deployment)
# Build and run containerized version
docker build -t moon-base-camp .
docker run -p 8000:8000 moon-base-camp
```

---

## Usage

### Navigation

1. **Start at Dashboard:** Open `index.html` to see the Mission Control Dashboard
2. **Select Module:** Click any module card to launch that simulator
3. **Configure Parameters:** Adjust input fields with your desired values
4. **Run Simulation:** Click "Activeer Systemen" or "Launch" button
5. **Review Results:** Check output cards for calculated metrics
6. **Return Home:** Use "← Back to Dashboard" navigation link

### Module Workflows

#### Algen Bioreactor
1. Set number of astronauts and oxygen consumption rate
2. Adjust algae concentration and production factor
3. Click "Activeer Systemen" to calculate
4. Review water volume, algae mass, and efficiency metrics

#### Catapult Simulation
1. Input object mass and desired launch velocity
2. Set gravity level (Moon: -1.62 m/s²)
3. Choose launch angle (0-90°)
4. Click "Launch Catapult" to simulate
5. Review trajectory graph and data points
6. Adjust parameters and re-run for optimization

#### Centrifuge Simulator
1. Input desired radius for rotation
2. Set target gravity level
3. Enter object mass
4. View calculated angular velocity, frequency, and forces
5. Adjust parameters to optimize for crew comfort

#### Lunar Map Explorer
1. Use map controls to pan and zoom
2. Click/drag to explore different regions
3. Identify terrain features and valleys
4. Note coordinates for settlement suitability analysis

#### Settlement Suitability
1. Adjust slider controls for elevation range
2. Set solar illumination requirements
3. Configure temperature and slope constraints
4. View color-coded suitability map
5. Identify optimal settlement zones meeting all criteria

---

## File Descriptions

### Core Files

| File | Purpose | Language |
|------|---------|----------|
| `index.html` | Landing page with module navigation | HTML |
| `style.css` | Global styles and theming | CSS |

### Simulation Modules

| Module | File | Focus | Language |
|--------|------|-------|----------|
| Bioreactor | `Algen.html` | Life support systems | HTML/JS |
| Catapult | `CatapultSimulation.html` | Ballistics & trajectories | HTML/JS |
| Centrifuge | `centrifuge.html` | Artificial gravity | HTML/JS |
| Lunar Map | `MoonMap.html` | Topographic visualization | HTML/JS + Leaflet |
| Habitability | `Habitability.html` | GIS site selection | HTML/JS |

### Backend Services

| File | Purpose | Language | Framework |
|------|---------|----------|-----------|
| `moonheightmap.py` | WMS proxy for lunar data | Python | Flask |

---

## Learning Objectives

This platform addresses key educational concepts:

### Physics
- Projectile motion and ballistics
- Circular motion and centripetal forces
- Energy conservation and kinetic energy
- Gravity and orbital mechanics

### Biology
- Photosynthetic oxygen production
- Life support system design
- Resource consumption calculations
- Sustainable habitat requirements

### Geography & Geology
- Topographic analysis and mapping
- Terrain feature identification
- Site selection criteria
- Environmental constraints

### Engineering
- System design and optimization
- Multi-criteria decision analysis (MCDA)
- Resource planning and allocation
- Structural analysis (centrifuge design)

### Space Science
- Lunar environment characteristics
- NASA/USGS data utilization
- Actual lunar conditions and parameters
- Settlement planning methodology

---

## Customization & Extension

### Adding New Modules

1. Create new HTML file (e.g., `NewModule.html`)
2. Link to `style.css` for consistent theming
3. Add navigation button in `index.html`
4. Include back-to-dashboard link in new module
5. Implement calculations using JavaScript

### Modifying Parameters

All input values and calculations are in the HTML/JS files:
- Search for `value="X"` to find default input values
- Modify calculation formulas in JavaScript `<script>` sections
- Update output labels and descriptions as needed

### Styling

Global CSS variables are defined in `style.css`:
```css
:root {
    --primary: #2563eb;           /* Main color (blue) */
    --success: #16a34a;           /* Success color (green) */
    --background: #f8fafc;        /* Page background */
    --card-bg: #ffffff;           /* Card background */
    --text-main: #1e293b;         /* Main text color */
    --text-muted: #64748b;        /* Muted text color */
    --border: #e2e8f0;            /* Border color */
}
```

Modify these values to change the entire site's color scheme.

---

## Data Attribution

### USGS Lunar Data
- **Source:** USGS Planetary Maps (https://planetarymaps.usgs.gov/)
- **Service:** Web Map Service (WMS)
- **Dataset:** LOLA (Lunar Orbiter Laser Altimeter) elevation color mapping
- **Resolution:** Meter-scale topographic accuracy
- **License:** Public domain (U.S. Government)

### Creative Commons License
This project is licensed under the **CC BY-NC-SA 4.0** (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International)

**You are free to:**
- ✅ Share — copy and redistribute the material
- ✅ Adapt — remix, transform, and build upon the material

**Under the following terms:**
- 🔗 **Attribution** — Credit must be given to the original creators
- 💼 **NonCommercial** — Material cannot be used for commercial purposes
- 🔄 **ShareAlike** — Derivative works must use the same license

---

## License

```
Einstein Moon Base Camp
© 2026 by Einstein Atheneum
Licensed under CC BY-NC-SA 4.0
https://creativecommons.org/licenses/by-nc-sa/4.0/
```

**License Attribution:**
- CC (Creative Commons) - https://creativecommons.org/
- BY (Attribution Required)
- NC (Non-Commercial Use Only)
- SA (Share-Alike)

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure:
- Code follows existing style conventions
- New features include proper documentation
- All calculations are physically accurate
- Responsive design is maintained

---

## Troubleshooting

### Lunar Map Not Loading
- Check internet connection (WMS tiles require online access)
- Verify USGS WMS service is accessible
- Clear browser cache and refresh
- Try alternative browser

### Calculations Not Working
- Check browser console for JavaScript errors (F12)
- Ensure JavaScript is enabled
- Try clearing browser cache
- Verify input values are valid numbers

### Performance Issues
- Close unnecessary browser tabs
- Clear browser cache
- Try a different browser
- Disable browser extensions

---

## Support & Contact

For questions, issues, or suggestions:
- **GitHub:** [Pieter-Smets/Einstein-Moon-Base-Camp](https://github.com/Pieter-Smets/Einstein-Moon-Base-Camp)
- **Institution:** Einstein Atheneum
- **License:** See LICENSE file for full terms

---

## Changelog

### Version 1.0.0 (Current)
- ✨ Initial release with 5 main modules
- 🌙 Lunar Map Explorer with USGS WMS integration
- 🚀 Catapult trajectory simulator with physics engine
- 🔄 Centrifuge simulator for artificial gravity
- 🌿 Algae bioreactor life support calculator
- 📍 GIS-based settlement suitability analyzer
- 🎨 Modern responsive UI with dark mode support
- 📱 Mobile-friendly design
- ♿ Accessibility features

---

## Roadmap

Planned features for future releases:
- [ ] Water extraction and processing module
- [ ] Power generation (solar/nuclear) calculator
- [ ] Radiation shielding analysis
- [ ] Thermal management simulator
- [ ] 3D habitat visualization
- [ ] Multiplayer collaborative simulations
- [ ] Mobile native apps
- [ ] Internationalization (i18n) support
- [ ] Advanced data export (CSV, PDF)
- [ ] Real-time collaboration features

---

## References & Further Reading

### Lunar Science
- [NASA Lunar Reconnaissance Orbiter (LRO)](https://lunar.gsfc.nasa.gov/)
- [USGS Astrogeology Science Center](https://astrogeology.usgs.gov/)
- [Lunar Surface Science Institute](https://lunarscience.nasa.gov/)

### Physics Education
- [MIT OpenCourseWare - Classical Mechanics](https://ocw.mit.edu/)
- [Khan Academy - Physics](https://www.khanacademy.org/science/physics)

### Space Settlement
- [NASA Moon to Mars Architecture](https://www.nasa.gov/artemis/)
- [Lunar Gateway Program](https://www.nasa.gov/humans/lunar-gateway/)

### GIS & Spatial Analysis
- [Leaflet.js Documentation](https://leafletjs.com/)
- [USGS Web Map Service](https://www.usgs.gov/products/web-services)

---

**Made with ❤️ for space exploration and STEM education**

*Last Updated: June 2026*
