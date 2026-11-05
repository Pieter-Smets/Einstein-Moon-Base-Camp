# Einstein Moon Base Camp 🌙

Einstein Moon Base Camp is an interactive educational site for exploring how a lunar habitat might work. The project combines a mission-control dashboard with a set of simulation modules covering life support, transportation, artificial gravity, communications, base layout, terrain exploration, and settlement planning.

**Live Demo:** [Einstein Moon Base Camp](https://pieter-smets.github.io/Einstein-Moon-Base-Camp/)

---

## Overview

This project is designed as a lightweight browser-based learning environment for students and hobbyists. It brings together multiple Moon-colony concepts into one dashboard so users can test assumptions, compare engineering options, and explore the challenges of living and operating on the lunar surface.

The main themes covered are:

- Life support and oxygen generation
- Lunar launch and payload delivery
- Artificial gravity via rotation
- Communication line-of-sight and signal interference
- Moonbase architecture and module planning
- Terrain exploration using lunar map data
- Habitat site suitability analysis

---

## Mission Control Dashboard

The entry page is `index.html`, which acts as the control center for the project. It presents a set of module cards, each linking to a different simulator or exploration page.

Current dashboard modules include:

- `Algen.html` — Algae Bioreactor
- `CatapultSimulation.html` — Catapult Trajectory
- `centrifuge.html` — Centrifuge Simulator
- `Communication.html` — Communication Simulator
- `moonbase.html` — Moonbase Overview
- `MoonMap.html` — Lunar Map Explorer

---

## Features

### 1. Algae Bioreactor 🌿
**File:** `Algen.html`

This module estimates how much algae and water are needed to support an astronaut crew with oxygen production. It includes adjustable inputs for oxygen demand, crew size, algal concentration, and productivity. The page calculates the required algae mass and water volume and visualizes the system as an animated bioreactor.

Key concepts:
- Photosynthetic oxygen production
- Crew life-support needs
- Resource sizing for lunar habitats
- Dynamic simulation of a closed-loop system

### 2. Catapult Trajectory 🚀
**File:** `CatapultSimulation.html`

This simulation models a lunar payload launch under custom gravity and launch conditions. Users can set mass, initial velocity, gravity, and angle, then view calculated values such as kinetic energy, flight time, range, and other trajectory parameters.

Key concepts:
- Projectile motion
- Lunar gravity effects
- Energy and range calculations
- Motion analysis for cargo delivery systems

### 3. Centrifuge Simulator 🔄
**File:** `centrifuge.html`

This module calculates key values for a rotating habitat or centrifuge, including angular velocity, frequency, period, and speed. It is designed to help users understand how artificial gravity can be created through rotation.

Key concepts:
- Circular motion
- Centripetal acceleration
- Artificial gravity design
- Rotation rate optimization

### 4. Communication Simulator 📡
**File:** `Communication.html`

This page models lunar communication by showing how antenna height, rover distance, and terrain curvature affect line-of-sight. It includes a visual graph of the Moon surface with a mast, rover, and signal path, and displays whether the link is optimal, weak, or broken.

Key concepts:
- Line-of-sight limits on the Moon
- Horizon blockage by curvature
- Regolith-related signal interference
- Practical communications constraints for lunar missions

### 5. Moonbase Overview 🏠
**File:** `moonbase.html`

This interactive page presents a conceptual Moonbase layout with selectable modules such as communication, energy, nutrition, living space, shielding, and underground systems. Each section includes a short explanation and supporting facts, making it useful as a design overview for the larger habitat concept.

Key concepts:
- Habitat zoning
- Module-based base design
- Systems integration
- Human survival infrastructure on the Moon

### 6. Lunar Map Explorer 🌑
**File:** `MoonMap.html`

This page uses Leaflet.js and USGS NASA WMS lunar map layers to visualize the Moon's terrain. It supports multiple base layers, zooming, panning, and coordinate navigation. It is intended for terrain inspection and mission planning.

Key concepts:
- Lunar topography
- Elevation data interpretation
- Map-based site review
- Terrain awareness for settlement planning

### 7. Settlement Suitability GIS 📍
**File:** `Habitability.html`

This page performs a simplified habitat suitability analysis by comparing terrain variables such as elevation and slope influence. It includes a heatmap view, a terrain map toggle, and a communication status badge. The interface allows users to explore how different terrain weights affect a candidate site.

Key concepts:
- Terrain suitability analysis
- Multi-factor mission planning
- Habitat placement decisions
- Environmental trade-offs

---

## Project Structure

```text
Einstein-Moon-Base-Camp/
├── index.html                # Mission-control dashboard
├── Algen.html                # Algae bioreactor simulator
├── CatapultSimulation.html   # Payload launch and trajectory calculator
├── centrifuge.html           # Artificial gravity simulator
├── Communication.html        # Lunar communications line-of-sight simulator
├── moonbase.html             # Moonbase design overview and module explorer
├── MoonMap.html              # Lunar terrain map explorer
├── Habitability.html         # Settlement suitability analysis page
├── manifest.json             # PWA manifest
├── sw.js                     # Service worker for installability
├── style.css                # Shared styling for the site
├── moonheightmap.py          # Optional Python helper for map-related work
├── README.md                 # Project overview and instructions
└── LICENSE                   # Project license if present in the repo
```

---

## How to Run

### Option 1: Open directly in a browser

Clone or download the repository and open `index.html` in a modern browser.

```bash
git clone https://github.com/Pieter-Smets/Einstein-Moon-Base-Camp.git
cd Einstein-Moon-Base-Camp
start index.html
```

### Option 2: Serve locally

For a more reliable setup, serve the folder with a local web server:

```bash
cd Einstein-Moon-Base-Camp
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

> Some modules load external resources and map tiles from the internet, so an active network connection is recommended.

---

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Leaflet.js
- USGS / NASA lunar map services
- Service worker support for light PWA behavior

---

## Educational Use

This project is intended for educational exploration rather than precise engineering validation. The calculators are simplified and designed to communicate the relationships between variables and mission design trade-offs. They are useful for demonstrating core ideas in space systems and lunar habitat design.

---

## License

This project is published under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license, as indicated in the site footer.

For more information, see:
https://creativecommons.org/licenses/by-nc-sa/4.0/

---

## Notes

- The dashboard is the main entry point for the site.
- Pages are designed as lightweight static web modules.
- The project is best viewed in a modern browser with JavaScript enabled.
- Map-based features depend on remote services and may vary based on network availability.

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
- Multi-criteria decision analysis
- Resource planning and allocation
- Structural analysis for rotating habitats

### Space Science
- Lunar environmental characteristics
- NASA/USGS data utilization
- Mission planning under real lunar constraints
- Settlement layout and systems integration

---

## Conclusion

Einstein Moon Base Camp is a compact educational toolkit for thinking through the systems required to support human life on the Moon. It brings together scientific, engineering, and planning concepts in a form that is easy to explore interactively from a browser.

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
