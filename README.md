# 🛡️ AI-GIS Flood Vulnerability & Public Welfare Prioritization System

### AI-GIS-FVWPS

**AI-GIS Based Flood Vulnerability and Public Welfare Prioritization System for Underserved Communities**

> An AI + GIS decision-support prototype that identifies flood-vulnerable and underserved communities, ranks them by public-welfare priority, visualizes risk spatially, and generates practical response recommendations for disaster-management decision makers.

---

## 🚀 OOSC 4.0 — Phase 1 Prototype Submission

This project is developed as a functional prototype for the **OOSC 4.0 Hackathon at IIIT Allahabad**.

The system combines:

* 🗺️ Geographic Information Systems (GIS)

* 🤖 Machine Learning

* 🧠 Generative AI

* 🌊 Flood exposure analysis

* 🏥 Essential-service accessibility analysis

* 👥 Population exposure

* 💧 Water and drainage infrastructure gaps

* 🏘️ Underserved-community identification

* 📊 Public welfare prioritization

* 🌐 Multilingual decision support

The objective is not simply to show where flooding occurs.

The system attempts to answer the more important disaster-management question:

> **"Which communities should receive attention first, why, and what essential services should be prioritized?"**

---

# 🔗 Prototype & Submission Links

| Resource             | Link                                                                     |

| -------------------- | ------------------------------------------------------------------------ |

| 🌐 Live Prototype    | https://karthikeyanravikumar-ds-ai-gis-fvwps-app-aomepe.streamlit.app/  |

| 💻 GitHub Repository | https://github.com/karthikeyanravikumar-ds/AI-GIS-FVWPS                 |

| 🎥 Demo Video        | https://youtu.be/fXOyZhNUklY                                            |

| 📄 Hackathon         | OOSC 4.0 — IIIT Allahabad                                               |

### Local Prototype

If the hosted prototype is unavailable, the application can be executed locally using the instructions provided below.

---

# 🎯 Problem Statement

Flood management systems often focus primarily on **hazard mapping** — identifying areas that are likely to experience flooding.

However, flood impact is not determined by flood exposure alone.

Two villages can experience similar flood exposure while having very different levels of:

* population exposure,

* healthcare accessibility,

* drinking-water availability,

* drainage infrastructure,

* road connectivity,

* proximity to rivers,

* essential-service gaps,

* and overall socioeconomic vulnerability.

This creates a critical decision-support problem:

> **How can disaster-management authorities identify which communities are most vulnerable and prioritize limited public resources accordingly?**

AI-GIS-FVWPS addresses this problem by combining spatial data, engineered vulnerability indicators, machine learning, and AI-assisted recommendations into a unified decision-support dashboard.

---

# 💡 Proposed Solution

AI-GIS-FVWPS converts village-level spatial and socioeconomic information into an integrated **Flood Vulnerability + Public Welfare Priority assessment**.

The system follows this pipeline:

```text

Raw GIS / Village Data

        │

        ▼

Data Cleaning & Validation

        │

        ▼

Feature Engineering

        │

        ├── Flood Exposure

        ├── Population Exposure

        ├── Healthcare Gap

        ├── Water Gap

        ├── Drainage Gap

        └── River Vulnerability

        │

        ▼

ML Vulnerability Segmentation

        │

        ▼

Underserved Community Score

        │

        ▼

Public Welfare Priority Score

        │

        ▼

Priority Classification & Ranking

        │

        ▼

GIS Visualization

        │

        ▼

Generative AI Decision Support

        │

        ▼

Recommended Welfare / Response Actions

```

---

# 🧠 What Makes the Prototype Different?

Traditional flood maps answer:

> **Where is the flood risk?**

AI-GIS-FVWPS attempts to answer:

> **Where is the risk, who is most vulnerable, what services are missing, and where should intervention be prioritized?**

The system therefore moves from:

**Hazard Mapping → Vulnerability Assessment → Welfare Prioritization → Decision Support**

This makes the prototype more relevant to real-world disaster-management workflows.

---

# ⭐ Core Features

## 1. 🗺️ Interactive GIS Command Center

The application provides an interactive geospatial dashboard built using **Folium + Streamlit**.

Users can explore:

* District boundaries

* Village boundaries

* Flood inundation zones

* River networks

* Hospitals

* Roads

* Village priority levels

* Selected village locations

The map supports multiple basemap options:

* CartoDB Positron

* OpenStreetMap

* Satellite imagery

Users can toggle GIS layers according to their analytical requirement.

The selected village is automatically highlighted and the map can zoom into the selected location.

---

# 2. 🌊 Flood Exposure Analysis

Flood exposure is converted into a normalized vulnerability indicator.

The system calculates:

```text

Flood Exposure

        ↓

Flood Score (0–100)

```

A higher score represents greater flood exposure relative to the study dataset.

This forms one of the primary components of the overall vulnerability and welfare-priority pipeline.

---

# 3. 👥 Population Exposure

Population information is transformed into a spatial exposure indicator.

The system derives:

```text

Population Density

=

Total Population / Village Area

```

The resulting population-density measure is normalized into a:

```text

Population Exposure Score

```

Higher population exposure increases the potential impact of a flood event.

---

# 4. 🏥 Healthcare Accessibility Gap

Healthcare accessibility is represented using distance to hospitals.

The system derives:

```text

Hospital Distance

        ↓

Healthcare Gap Score

```

Greater distance from healthcare facilities results in greater vulnerability.

This enables the system to identify communities where flood exposure is combined with poor healthcare accessibility.

---

# 5. 💧 Drinking-Water Infrastructure Gap

The feature-engineering pipeline considers available water infrastructure, including available fields such as:

* Tap water

* Hand pumps

* Tubewells

* Wells

* Tanks / lakes

The system derives:

```text

Water Availability

        ↓

Water Infrastructure Score

        ↓

Water Gap Score

```

Lower availability increases the water-access vulnerability.

---

# 6. 🚰 Drainage Infrastructure Gap

Drainage infrastructure is incorporated into the vulnerability assessment.

The system considers drainage-related attributes such as:

* Open drainage

* Covered drainage

The resulting availability measure is converted into a:

```text

Drainage Gap Score

```

This helps distinguish communities where flood exposure is accompanied by weaker drainage infrastructure.

---

# 7. 🌊 River Proximity Vulnerability

Distance from rivers is incorporated into the model.

The system derives:

```text

River Distance

        ↓

River Vulnerability Score

```

Closer proximity to rivers produces greater river-related vulnerability.

This provides an additional spatial factor beyond direct flood exposure.

---

# 8. 🤖 Machine Learning Vulnerability Segmentation

The project includes an unsupervised machine-learning pipeline using **K-Means clustering**.

The ML pipeline uses vulnerability-related features including:

```text

• Flood Score

• Population Score

• Healthcare Gap Score

• Water Gap Score

• Drainage Gap Score

• River Vulnerability Score

```

Before clustering:

1. Numerical conversion is performed.

2. Missing values are handled using median imputation.

3. Features are standardized using `StandardScaler`.

4. Multiple K-Means configurations are evaluated.

The implementation evaluates:

```text

K = 2

K = 3

K = 4

K = 5

```

and selects the configuration with the best silhouette score.

This allows the system to discover groups of villages exhibiting similar vulnerability characteristics rather than relying only on manually assigned categories.

---

# 9. 🏘️ Underserved Community Identification

A dedicated underserved-community score is calculated using:

```text

Service Gap        = 50%

Population         = 30%

Flood Exposure     = 20%

```

Conceptually:

```text

Underserved Score

=

0.50(Service Gap)

+

0.30(Population Exposure)

+

0.20(Flood Exposure)

```

The score is normalized to a `0–100` range.

This allows the system to identify communities where vulnerability is amplified by inadequate access to essential services.

---

# 10. 🎯 Public Welfare Priority Score

The central decision-support component is the **Welfare Priority Score**.

The current prototype combines:

| Factor                | Weight |

| --------------------- | -----: |

| Flood Vulnerability   |    40% |

| Essential Service Gap |    30% |

| Population Exposure   |    20% |

| Underserved Condition |    10% |

The resulting score is:

```text

Welfare Priority Score

=

0.40(Flood Vulnerability)

+

0.30(Service Gap)

+

0.20(Population Exposure)

+

0.10(Underserved Score)

```

The final score is constrained to:

```text

0 – 100

```

This score becomes the basis for ranking communities for welfare-oriented intervention.

---

# 🚨 Priority Classification

Villages are classified according to their welfare-priority score.

|    Score | Priority    |

| -------: | ----------- |

|   75–100 | 🔴 Critical |

| 50–74.99 | 🟠 High     |

| 25–49.99 | 🟡 Moderate |

|  0–24.99 | 🟢 Low      |

The system also generates a **priority rank**, allowing authorities to identify the highest-priority communities across the study area.

---

# 🏥💧🚰 Priority Service Identification

The welfare pipeline identifies services that may require attention based on actual service-gap indicators.

Potential priority areas include:

* Healthcare

* Drinking water

* Drainage

* Emergency response

* Evacuation support

* Food supplies

* Road/connectivity

* Other public-welfare interventions

This creates a bridge between:

```text

Risk Assessment

        ↓

Service Deficiency

        ↓

Actionable Priority

```

---

# 🧠 AI Copilot

The prototype integrates a **Generative AI decision-support layer using Google Gemini**.

The AI does **not** independently calculate the vulnerability score.

Instead:

```text

GIS + ML Pipeline

        ↓

Calculated Village Assessment

        ↓

Gemini AI

        ↓

Human-readable Decision Support

```

The AI receives the already-calculated village assessment and generates:

* Risk summary

* Priority reason

* Key risk factors

* Priority services

* Recommended actions

* Urgency

* Public welfare message

The implementation explicitly instructs the AI to:

* use only supplied village data,

* not invent statistics,

* not modify calculated scores,

* distinguish calculated factors from recommendations,

* avoid claiming future flood prediction without prediction data,

* provide practical disaster-management recommendations.

This separation is intentional.

### Principle

> **Machine Learning calculates. GIS visualizes. Generative AI explains and recommends.**

---

# 🌐 Multilingual Decision Support

The dashboard supports:

* 🇬🇧 English

* 🇮🇳 Marathi

* 🇮🇳 Hindi

The language selector changes the dashboard interface and AI-generated assessment language.

This is particularly important for public-sector and community-facing disaster-management applications where English-only interfaces can limit accessibility.

---

# 📊 Analytics Dashboard

The analytics section provides a village-level assessment of:

### Risk Contribution

* Flood contribution

* Population contribution

* Service-gap contribution

* River vulnerability contribution

### Infrastructure Deficits

* Healthcare gap

* Water gap

* Drainage gap

The dashboard converts these indicators into visual analytics so that decision makers can quickly understand **why a village has been prioritized**.

---

# 📑 Dataset Ledger

The application includes a dataset-oriented view containing:

* Priority rank

* Village

* District

* Welfare priority

* Vulnerability score

* Flood exposure

* Hospital distance

* Service-gap score

The filtered dataset can also be exported as CSV.

This provides a simple mechanism for downstream analysis and reporting.

---

# 🏗️ System Architecture

```text

                   ┌──────────────────────┐

                   │   GIS / Village Data │

                   └──────────┬───────────┘

                              │

                              ▼

                   ┌──────────────────────┐

                   │ Data Cleaning        │

                   │ & Validation         │

                   └──────────┬───────────┘

                              │

                              ▼

                   ┌──────────────────────┐

                   │ Feature Engineering  │

                   └──────────┬───────────┘

                              │

             ┌────────────────┼────────────────┐

             │                │                │

             ▼                ▼                ▼

       Flood Score     Population Score   Service Gaps

             │                │                │

             └────────────────┼────────────────┘

                              │

                              ▼

                   ┌──────────────────────┐

                   │ K-Means ML           │

                   │ Vulnerability        │

                   │ Segmentation         │

                   └──────────┬───────────┘

                              │

                              ▼

                   ┌──────────────────────┐

                   │ Underserved Score    │

                   └──────────┬───────────┘

                              │

                              ▼

                   ┌──────────────────────┐

                   │ Welfare Priority     │

                   │ Score + Ranking      │

                   └──────────┬───────────┘

                              │

                ┌─────────────┴─────────────┐

                ▼                           ▼

      ┌──────────────────┐        ┌──────────────────┐

      │ Interactive GIS  │        │ Gemini AI Copilot│

      │ Visualization    │        │ Recommendations  │

      └────────┬─────────┘        └────────┬─────────┘

               │                           │

               └─────────────┬─────────────┘

                             ▼

                 ┌────────────────────────┐

                 │ Disaster Management    │

                 │ Decision Support       │

                 └────────────────────────┘

```

---

# 🔄 End-to-End Workflow

### Step 1 — Data Collection

The system receives village-level spatial, demographic, infrastructure and flood-related information.

### Step 2 — Data Cleaning

The preprocessing pipeline:

* removes completely empty columns,

* removes duplicate records,

* standardizes missing-value representations,

* converts relevant attributes to numeric form.

### Step 3 — Feature Engineering

The system derives:

* population density,

* water availability,

* drainage availability,

* flood score,

* population score,

* healthcare gap,

* water gap,

* drainage gap,

* service gap,

* river vulnerability.

### Step 4 — ML Segmentation

K-Means clustering groups villages based on their vulnerability characteristics.

### Step 5 — Vulnerability Assessment

The system calculates vulnerability-related indicators and interprets the resulting clusters.

### Step 6 — Welfare Prioritization

The system calculates:

* underserved score,

* welfare priority score,

* priority level,

* priority rank,

* priority services.

### Step 7 — GIS Visualization

Results are displayed spatially through interactive GIS layers.

### Step 8 — AI Decision Support

The selected village's calculated assessment is passed to the AI Copilot.

### Step 9 — Actionable Recommendations

The AI produces a concise decision-support assessment and practical response recommendations.

---

# 🧰 Technology Stack

## Programming

* Python

## Data Processing

* Pandas

* NumPy

## Machine Learning

* Scikit-learn

* K-Means Clustering

* StandardScaler

* Silhouette Score

## GIS / Geospatial Visualization

* Folium

* GeoJSON

* Streamlit-Folium

## Dashboard

* Streamlit

## Data Visualization

* Plotly

## Generative AI

* Google Gemini API

* `google-genai`

## Configuration

* Python Dotenv

The repository's current dependency file pins the main application stack, including Streamlit, Folium, Streamlit-Folium, Plotly/Altair ecosystem dependencies, NumPy, Pandas, Scikit-learn, and Google GenAI packages.

---

# 📁 Repository Structure

```text

AI-GIS-FVWPS/

│

├── app.py

│

├── requirements.txt

│

├── data/

│   ├── external/

│   │   ├── study_area_3districts.geojson

│   │   ├── village_ai_final.geojson

│   │   ├── village_flooded_area_district.geojson

│   │   ├── river_network_in_district.geojson

│   │   ├── hospitals_3districts.geojson

│   │   └── road.geojson

│   │

│   ├── health.csv

│   ├── village_ai_ml_final.csv

│   └── village_ai_ml_health.csv

│

├── src/

│   ├── __init__.py

│   ├── config.py

│   ├── data_loader.py

│   ├── feature_engineering.py

│   ├── gemini_ai.py

│   ├── i18n.py

│   ├── main.py

│   ├── merge_health.py

│   ├── vulnerability_model.py

│   └── welfare_priority.py

│

└── .gitignore

```

The current repository contains dedicated modules for configuration, data loading, feature engineering, Gemini integration, internationalization, vulnerability modelling, health-data merging and welfare prioritization.

---

# ⚙️ Installation

## 1. Clone the repository

```bash

git clone https://github.com/karthikeyanravikumar-ds/AI-GIS-FVWPS.git

cd AI-GIS-FVWPS

```

---

## 2. Create a virtual environment

### Windows

```bash

python -m venv .venv

.venv\Scripts\activate

```

### macOS / Linux

```bash

python3 -m venv .venv

source .venv/bin/activate

```

---

## 3. Install dependencies

```bash

pip install -r requirements.txt

```

The repository currently provides a pinned `requirements.txt`, including the required Streamlit, Folium, GIS visualization, machine-learning and Google GenAI dependencies.

---

# 🔐 Gemini API Configuration

The AI Copilot requires a Gemini API key.

Create a file named:

```text

.env

```

in the project root.

Add:

```env

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

```

### Important

Do **not** commit your `.env` file or expose your API key publicly.

The application explicitly loads the API key from the project `.env` file before initializing the Gemini client.

---

# ▶️ Run the Prototype

Start the Streamlit application:

```bash

streamlit run app.py

```

The terminal will provide a local URL similar to:

```text

http://localhost:8501

```

Open the URL in your browser.

---

# 🖥️ Prototype Walkthrough

Once the dashboard opens:

### 1. Select Language

Choose:

```text

English

Marathi

Hindi

```

### 2. Select District

Use the district filter to narrow the study area.

### 3. Select Priority

Filter villages by:

```text

All

High

Moderate

Low

```

### 4. Select a Village

Choose a target village to inspect its assessment.

### 5. Explore the GIS Map

Toggle:

```text

Flood Zones

Rivers

Hospitals

Roads

```

### 6. Inspect Risk Indicators

Review:

* Flood Exposure

* Vulnerability Index

* Welfare Priority Score

* Hospital Distance

* Service Gap

### 7. Open Analytics

Understand the contribution of:

* flood exposure,

* population,

* service gaps,

* river vulnerability.

### 8. Open AI Copilot

Generate a village-specific AI assessment and recommended actions.

### 9. Inspect Dataset Ledger

Review and export the filtered village-level dataset.

---

# 📌 Example Decision-Support Flow

A decision maker selects a village.

The system may reveal:

```text

Village

   ↓

High flood exposure

   ↓

High population exposure

   ↓

Large hospital distance

   ↓

Poor water / drainage infrastructure

   ↓

High service gap

   ↓

High welfare priority

   ↓

Priority services identified

   ↓

AI-generated response recommendations

```

The goal is to turn a complex collection of GIS and tabular indicators into a single interpretable decision-support workflow.

---

# 🔬 Technical Methodology

## Normalization

Most vulnerability indicators are converted into a `0–100` scale using Min-Max normalization.

Conceptually:

```text

Score =

((Value - Minimum) /

(Maximum - Minimum)) × 100

```

Missing values are handled through median imputation where appropriate.

---

## Machine Learning

The ML pipeline uses:

```text

StandardScaler

       ↓

K-Means

       ↓

K = 2...5 evaluation

       ↓

Silhouette Score

       ↓

Best K

       ↓

Village Clusters

```

The clustering implementation evaluates candidate cluster counts from 2 through 5 and selects the configuration with the strongest silhouette score.

---

# 🎯 Welfare Prioritization Methodology

The welfare-priority model is intentionally interpretable.

```text

                    FLOOD

                     40%

                      │

                      ▼

SERVICE GAP 30% ──► PRIORITY ◄── POPULATION 20%

                      ▲

                      │

                 UNDERSERVED

                    10%

```

This design makes it possible for a decision maker to understand **why** a community receives a particular priority score rather than relying on an opaque black-box prediction.

The implemented scoring logic explicitly combines flood vulnerability, service gaps, population exposure and underserved conditions.

---

# 🤖 Responsible AI Design

The Generative AI component is designed as a **decision-support layer**, not as the source of the underlying risk calculation.

### AI receives:

* Village information

* District

* Calculated vulnerability indicators

* Welfare score

* Service gaps

* Priority services

* Other supplied assessment attributes

### AI produces:

* Risk summary

* Priority explanation

* Key risk factors

* Recommended actions

* Urgency

* Public-welfare message

### AI does NOT:

* independently calculate the official vulnerability score,

* modify the ML-derived priority score,

* invent statistics,

* claim future flood prediction without prediction data,

* provide medical diagnosis.

This separation reduces the risk of presenting generated text as if it were the underlying analytical calculation. The repository's Gemini system prompt explicitly enforces these constraints.

---

# 🌍 Scalability

Although the current prototype focuses on a defined study region, the architecture is designed around reusable village-level features.

The same pipeline can theoretically be extended to:

```text

One village

      ↓

Multiple villages

      ↓

Multiple districts

      ↓

Entire state

      ↓

Multiple states

      ↓

National disaster-management datasets

```

The key scalability mechanism is the separation between:

```text

Data

 ↓

Feature Engineering

 ↓

ML

 ↓

Prioritization

 ↓

Visualization

 ↓

AI Explanation

```

This makes individual components easier to replace or upgrade without redesigning the entire application.

---

# 📈 Future Scalability

Potential future extensions include:

### Real-Time Flood Monitoring

Integration with:

* rainfall data,

* river-level sensors,

* weather APIs,

* satellite imagery,

* near-real-time flood observations.

### Predictive Flood Modelling

Future versions could incorporate:

* rainfall forecasting,

* river-level prediction,

* temporal flood modelling,

* time-series ML,

* remote-sensing based inundation prediction.

### Larger Geographic Coverage

The system can be expanded from the current prototype study area to:

* additional districts,

* entire Maharashtra,

* other Indian states,

* national-scale disaster-management applications.

### Resource Allocation Optimization

Future versions could recommend:

* evacuation-centre placement,

* ambulance allocation,

* relief-material distribution,

* emergency-team deployment,

* temporary healthcare facilities.

### Mobile / Field Application

A field application could allow officials or volunteers to:

* report local flooding,

* upload photographs,

* update infrastructure conditions,

* report blocked roads,

* report service outages.

---

# 🧪 Prototype Scope & Limitations

This is a **hackathon prototype and decision-support system**, not a certified disaster-management platform.

Important limitations include:

1. The current system uses prepared datasets rather than a complete real-time disaster-data infrastructure.

2. The current ML component performs vulnerability segmentation rather than future flood forecasting.

3. Welfare scores depend on the quality and coverage of the supplied datasets.

4. GIS accuracy depends on the underlying spatial datasets.

5. AI-generated recommendations should be reviewed by qualified authorities before operational use.

6. The prototype should not be interpreted as an official government risk classification.

These limitations are intentional and define the boundary between the current prototype and a production disaster-management system.

---

# 🔐 Security Considerations

* API credentials must be stored in `.env`.

* `.env` should remain excluded from Git.

* No API keys should be hard-coded into source files.

* Sensitive operational datasets should not be publicly committed.

* Production deployments should use secret-management services.

* AI-generated recommendations should remain subject to human review.

---

# 🧩 Design Principles

The project follows five main principles:

### 1. Explainability

Priority scores should be understandable.

### 2. Spatial Context

Risk should be interpreted geographically.

### 3. Human-Centered AI

AI should assist decision makers rather than replace them.

### 4. Welfare-Oriented Prioritization

The system focuses on people and essential services, not only physical flood exposure.

### 5. Modular Architecture

Data, ML, GIS, prioritization and AI components remain logically separated.

---

# 🏆 Innovation

The primary innovation of AI-GIS-FVWPS is the integration of multiple decision layers into one workflow:

```text

Flood Hazard

     +

Population Exposure

     +

Essential Services

     +

Infrastructure Gaps

     +

River Proximity

     +

ML Vulnerability Segmentation

     +

Underserved Communities

     +

Public Welfare Prioritization

     +

Generative AI

     =

AI-GIS Disaster Decision Support

```

Instead of producing another static flood-risk map, the prototype attempts to create a **prioritization engine for people-centric disaster response**.

---

# 🌐 Real-World Impact

The system is designed around a practical disaster-management scenario:

> Emergency resources are limited, but the number of vulnerable communities can be large.

The system can help decision makers move from:

```text

"These areas are flooded."

```

to:

```text

"These communities are most vulnerable,

these are the contributing factors,

these essential services are deficient,

and these communities should be considered

for priority intervention."

```

Potential stakeholders include:

* District disaster-management authorities

* Local government bodies

* Emergency response teams

* Public-health departments

* NGOs

* Relief organizations

* Infrastructure planners

* Community welfare organizations

---

# 🧭 Intended Users

### Government / Disaster Management

Identify and rank communities requiring attention.

### Emergency Response Teams

Understand spatial concentration of vulnerable communities.

### Public Health Authorities

Identify locations with healthcare-access gaps.

### NGOs & Relief Organizations

Prioritize welfare interventions.

### Urban / Rural Planners

Identify infrastructure deficits associated with vulnerability.

### Researchers

Experiment with AI, GIS and spatial vulnerability modelling.

---

# 🧪 Suggested Hackathon Demo Scenario

For the final presentation, demonstrate the system as a real decision-making workflow:

### Scenario

A disaster-management officer wants to identify communities requiring priority welfare intervention.

### Demonstration

```text

1. Open dashboard

        ↓

2. Select district

        ↓

3. Observe flood zones

        ↓

4. Select a village

        ↓

5. Review vulnerability score

        ↓

6. Review flood exposure

        ↓

7. Review hospital distance

        ↓

8. Review service gaps

        ↓

9. Review welfare priority

        ↓

10. Open AI Copilot

        ↓

11. Generate recommendations

        ↓

12. Switch language

        ↓

13. Export dataset

```

This demonstrates the entire value chain rather than only showing the map.

---

# 🛠️ Troubleshooting

## Streamlit command not found

Make sure the virtual environment is activated:

```bash

.venv\Scripts\activate

```

Then reinstall:

```bash

pip install -r requirements.txt

```

---

## Gemini API error

Check that:

```text

.env

```

exists in the project root and contains:

```env

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

```

Do not include quotation marks unless required by your environment.

---

## Dataset loading error

Verify that the expected project directories exist:

```text

data/

data/external/

outputs/

```

The dashboard expects its processed village dataset and GIS layers at the paths configured in `app.py`.

---

## GIS layers not appearing

Verify that the required GeoJSON files exist under:

```text

data/external/

```

Expected layers include:

```text

study_area_3districts.geojson

village_ai_final.geojson

village_flooded_area_district.geojson

river_network_in_district.geojson

hospitals_3districts.geojson

road.geojson

```

---

# 📚 Data & Methodology Transparency

The repository contains both tabular and geospatial data assets used by the prototype.

The data directory currently contains health-related data, village ML datasets and external GIS layers.

The preprocessing pipeline cleans duplicate and empty records and standardizes common missing-value representations before feature engineering.

The feature-engineering pipeline derives population, water, drainage, healthcare, flood and river-related indicators before generating vulnerability scores.

---

# 🔭 Future Vision

AI-GIS-FVWPS is intended as a foundation for a broader:

> **People-Centric AI Disaster Management Platform**

A mature production version could evolve into a continuously updated system combining:

```text

Satellite Data

      +

Rainfall

      +

River Sensors

      +

Weather Forecasts

      +

GIS

      +

Population Data

      +

Healthcare

      +

Infrastructure

      +

Machine Learning

      +

Generative AI

      ↓

Real-Time Disaster Decision Support

```

The long-term objective is to help authorities answer three questions:

### WHERE?

Where is the hazard and vulnerability concentrated?

### WHO?

Which communities are most exposed and underserved?

### WHAT NEXT?

What intervention should be prioritized?

---

# 👥 Team

Project: AI-GIS Flood Vulnerability & Public Welfare Prioritization System

Team Members & Contributions

🗺️ GIS Mapping — Karthikeyan

Developed and integrated the GIS layers, spatial visualization, flood-zone mapping, river, hospital and road layers.

🤖 Machine Learning & Scoring — Karthikeyan & Angel

Worked on vulnerability modelling, feature analysis, ML-based segmentation, welfare-priority scoring and interpretation.

🖥️ Streamlit & Interface — Kishore

Developed the Streamlit dashboard structure and user interface for interacting with the system and its analytical modules.

---

# 📜 License

Add the project's chosen open-source license before final submission.

Recommended for an open-source hackathon project:

```text

MIT License

```

If an MIT license is selected, add a `LICENSE` file containing the official MIT License text.

---

# ⭐ Acknowledgement

Built as an open-source AI + GIS prototype for **OOSC 4.0 — Opportunity Open Source Conference, IIIT Allahabad**.

The project aims to demonstrate how open-source geospatial technologies, machine learning and generative AI can be combined to create practical, explainable and people-centric disaster-management decision-support systems.

---

# 🔗 Project Links

* **GitHub:** https://github.com/karthikeyanravikumar-ds/AI-GIS-FVWPS

* **Live Prototype:** https://karthikeyanravikumar-ds-ai-gis-fvwps-app-aomepe.streamlit.app/

* **Demo Video:** https://youtu.be/fXOyZhNUklY

* **OOSC 4.0:** https://oosc.iiita.ac.in/hackathon

---

## 💬 One-Line Project Pitch

> **AI-GIS-FVWPS transforms flood maps into actionable welfare priorities by combining geospatial risk, population exposure, essential-service gaps, machine learning and generative AI to identify which underserved communities need attention first.**
