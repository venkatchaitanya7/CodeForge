# AgriLand Guard AI 🗺️🌾

> **AI-Assisted Land Boundary Verification & Precision Farm Management Platform**  
> *Measure clearly • Cultivate smartly • Verify responsibly.*

---

## 📌 Vision & Core Idea
**AgriLand Guard AI** is an all-in-one digital companion for agricultural landowners—especially small and marginal farmers. It bridges the gap between official digitized land records (Records of Rights / RoRs) and on-ground realities by enabling farmers to independently map plot boundaries, detect area discrepancies, and immediately translate verified plot dimensions into optimized cultivation budgets, crop advisories, and weather plans.

---

## 🚨 The Twin Challenges Solved
1. **Land Discrepancies & Border Conflicts:** Missing survey stones, complex Pahani/RoR documents, and adjoining farm boundaries often lead to unverified shortfalls or encroachments that escalate into civil disputes.
2. **Uncalibrated Farm Planning:** Farmers often estimate input costs (seeds, fertilizers, labor) blindly without knowing their precise workable acreage or matching it to localized weather and soil health.

---

## ✨ Integrated Feature Suite

### 1. 🗺️ Satellite Boundary Mapping & Discrepancy Detection (Core Engine)
* **Satellite Plotter:** Interactive GIS satellite mapping to trace boundary corners.
* **Geodesic Computation:** Real-time spherical polygon calculation (Acres, Guntas, and $m^2$) using Turf.js.
* **Tolerance & Discrepancy Flag:** Compares mapped ground area with legal title values. Highlights whether variance is within acceptable tolerance ($\pm3\%$) or requires official revenue review.
* **Revenue Advisory:** Step-by-step guidance on applying for official resurveys via state revenue portals (e.g., Mojini in Karnataka or MeeBhoomi in AP).

### 2. 📊 Land-Linked Cultivation Cost Calculator
* Dynamically pulls the **exact mapped plot acreage** from the GIS map.
* Estimates total expenditure: seeds, fertilizers, machinery, irrigation, and labor.
* Projects expected crop yield, gross revenue, and net profit before sowing.

### 3. 🌱 Parcel Crop & Fertilizer Advisor
* Recommends high-yield crops based on soil type, seasonal patterns, and water resources.
* Generates balanced N-P-K fertilizer guidelines tailored to the parcel.

### 4. 🌦️ Localized Weather & Rainfall Radar
* Real-time temperature, humidity, and 7-day rainfall forecasts.
* Automated irrigation advisories (e.g., "Skip watering today: 85% chance of rain").

### 5. 🍂 AI Crop Disease Diagnosis
* Rapid leaf image classification to diagnose crop diseases, severity levels, and organic treatment remedies.

### 6. 🗣️ Multilingual Voice Guidance
* Native voice assistance in **Kannada (ಕನ್ನಡ), English, Hindi (हिन्दी), Telugu (తెలుగు), Tamil (தமிழ்), and Malayalam (മലയാളം)** to make revenue and agronomic data accessible to rural farmers.

---

## 🛠️ Technology Stack
* **Frontend:** HTML5, Tailwind CSS, Modern JavaScript (Obsidian Dark GIS Theme)
* **GIS & Spatial Math:** Leaflet.js, Esri World Imagery, Turf.js
* **Backend:** Python (FastAPI / Flask) with GeoJSON support
* **AI/ML Extensions:** Lightweight CNN for leaf disease screening; Scikit-Learn for crop recommendation

---

## ⚠️ Responsible Tech Disclaimer
*AgriLand Guard AI provides map and GPS-based estimations for early awareness and planning. These do not constitute official legal determinations of land title or boundary lines. Final verification rests with authorized government land revenue authorities.*