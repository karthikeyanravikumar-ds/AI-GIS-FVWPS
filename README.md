🛡️ AI-GIS-FVWPS

AI-GIS Flood Vulnerability & Public Welfare Prioritization System

An AI + GIS decision-support prototype that identifies flood-vulnerable and underserved communities, ranks them by public-welfare priority, visualizes risk spatially, and generates practical response recommendations for disaster-management decision makers.

<p align="center">








</p>

<p align="center">
  <a href="https://karthikeyanravikumar-ds-ai-gis-fvwps-app-aomepe.streamlit.app/"><strong>🌐 Live Demo</strong></a> •
  <a href="https://youtu.be/fXOyZhNUklY"><strong>🎥 Demo Video</strong></a> •
  <a href="https://github.com/karthikeyanravikumar-ds/AI-GIS-FVWPS"><strong>💻 GitHub</strong></a>
</p>

🚀 OOSC 4.0 — Phase 1 Prototype

AI-GIS-FVWPS is a functional prototype developed for the OOSC 4.0 Hackathon at IIIT Allahabad.

The system combines:

🗺️ Geographic Information Systems (GIS)

🤖 Machine Learning

🧠 Generative AI

🌊 Flood exposure analysis

👥 Population exposure

🏥 Essential-service accessibility

💧 Water infrastructure gaps

🚰 Drainage infrastructure gaps

🏘️ Underserved-community identification

📊 Public welfare prioritization

🌐 Multilingual decision support

The Core Question

Traditional flood mapping mainly asks:

Where is the flood risk?

AI-GIS-FVWPS goes one step further:

Where is the risk, who is most vulnerable, what services are missing, and where should intervention be prioritized?

This moves the workflow from:

Hazard Mapping → Vulnerability Assessment → Welfare Prioritization → Decision Support

🔗 Prototype & Submission Links

Resource

Link

🌐 Live Prototype

Open Streamlit App

💻 GitHub Repository

AI-GIS-FVWPS

🎥 Demo Video

Watch on YouTube

🏆 Hackathon

OOSC 4.0 — IIIT Allahabad

🎯 Problem Statement

Flood management systems often focus on hazard mapping — identifying locations likely to experience flooding.

However, flood impact is not determined by exposure alone.

Two communities may experience similar flood exposure while having very different levels of:

Population exposure

Healthcare accessibility

Drinking-water availability

Drainage infrastructure

Road connectivity

River proximity

Essential-service availability

Overall vulnerability

This creates a practical decision-support problem:

How can disaster-management authorities identify the most vulnerable communities and prioritize limited public resources accordingly?

AI-GIS-FVWPS addresses this by combining spatial data, engineered vulnerability indicators, machine learning, welfare-priority scoring, and AI-assisted recommendations into one dashboard.

💡 Proposed Solution

The system converts village-level spatial, demographic, infrastructure, and flood-related information into an integrated:

Flood Vulnerability + Public Welfare Priority Assessment

End-to-End Pipeline

GIS / Village Data
        ↓
Data Cleaning & Validation
        ↓
Feature Engineering
        ├── Flood Exposure
        ├── Population Exposure
        ├── Healthcare Gap
        ├── Water Gap
        ├── Drainage Gap
        └── River Vulnerability
        ↓
ML Vulnerability Segmentation
        ↓
Underserved Community Score
        ↓
Welfare Priority Score
        ↓
Priority Classification & Ranking
        ↓
Interactive GIS Visualization
        ↓
Generative AI Decision Support
        ↓
Recommended Welfare / Response Actions

⭐ Core Features

1. 🗺️ Interactive GIS Command Center

Built with Folium + Streamlit, the dashboard provides interactive spatial analysis.

GIS layers include

District boundaries

Village boundaries

Flood inundation zones

River networks

Hospitals

Roads

Village priority levels

Selected village locations

Basemap options

CartoDB Positron

OpenStreetMap

Satellite imagery

Users can toggle layers, select villages, and zoom into the selected location.

2. 🌊 Flood Exposure Analysis

Flood exposure is converted into a normalized Flood Score (0–100).

Flood Exposure
      ↓
Flood Score
   0 — 100

A higher score represents greater flood exposure relative to the study dataset.

3. 👥 Population Exposure

Population exposure is derived from population density:

Population Density
=
Total Population / Village Area

The resulting measure is normalized into a Population Exposure Score.

Higher population exposure indicates potentially greater human impact during a flood event.

4. 🏥 Healthcare Accessibility Gap

Healthcare accessibility is represented using distance to hospitals.

Hospital Distance
        ↓
Healthcare Gap Score

Greater distance from healthcare facilities increases the vulnerability contribution.

5. 💧 Drinking-Water Infrastructure Gap

The feature-engineering pipeline considers available water infrastructure such as:

Tap water

Hand pumps

Tubewells

Wells

Tanks / lakes

Water Availability
        ↓
Water Infrastructure Score
        ↓
Water Gap Score

Lower availability increases water-access vulnerability.

6. 🚰 Drainage Infrastructure Gap

Drainage-related attributes include:

Open drainage

Covered drainage

These are converted into a Drainage Gap Score to distinguish communities where flood exposure is combined with weaker drainage infrastructure.

7. 🌊 River Proximity Vulnerability

Distance from rivers is incorporated into the assessment.

River Distance
      ↓
River Vulnerability Score

Closer proximity produces greater river-related vulnerability.

🤖 Machine Learning Vulnerability Segmentation

The project uses unsupervised K-Means clustering to identify groups of villages with similar vulnerability characteristics.

ML Features

Flood Score
Population Score
Healthcare Gap Score
Water Gap Score
Drainage Gap Score
River Vulnerability Score

Preprocessing

Convert relevant attributes to numeric form.

Handle missing values using median imputation.

Standardize features using StandardScaler.

Evaluate multiple K-Means configurations.

Candidate values:

K = 2
K = 3
K = 4
K = 5

The configuration with the strongest silhouette score is selected.

The ML component performs vulnerability segmentation; it does not claim to forecast future floods.

🏘️ Underserved Community Identification

A dedicated underserved-community score combines:

Factor

Weight

Service Gap

50%

Population Exposure

30%

Flood Exposure

20%

Formula

Underserved Score
=
0.50(Service Gap)
+ 0.30(Population Exposure)
+ 0.20(Flood Exposure)

The score is normalized to 0–100.

This helps identify communities where flood vulnerability is amplified by inadequate access to essential services.

🎯 Public Welfare Priority Score

The central decision-support component is the Welfare Priority Score.

Factor

Weight

Flood Vulnerability

40%

Essential Service Gap

30%

Population Exposure

20%

Underserved Condition

10%

Formula

Welfare Priority Score
=
0.40(Flood Vulnerability)
+ 0.30(Service Gap)
+ 0.20(Population Exposure)
+ 0.10(Underserved Score)

Final score:

0 — 100

The score is used to rank communities for welfare-oriented intervention.

🚨 Priority Classification

Score

Priority

75–100

🔴 Critical

50–74.99

🟠 High

25–49.99

🟡 Moderate

0–24.99

🟢 Low

The system also generates a priority rank, allowing users to identify the highest-priority communities within the study area.

🏥💧🚰 Priority Service Identification

The welfare pipeline identifies service areas that may require attention based on calculated service-gap indicators.

Potential intervention areas include:

Healthcare

Drinking water

Drainage

Emergency response

Evacuation support

Food supplies

Road / connectivity

Other public-welfare interventions

Risk Assessment
      ↓
Service Deficiency
      ↓
Actionable Priority

🧠 AI Copilot

The prototype integrates a Generative AI decision-support layer using Google Gemini.

Important Design Principle

Machine Learning calculates. GIS visualizes. Generative AI explains and recommends.

The AI does not independently calculate the official vulnerability or welfare score.

Instead:

GIS + ML Pipeline
       ↓
Calculated Village Assessment
       ↓
Gemini AI
       ↓
Human-readable Decision Support

AI generates

Risk summary

Priority reason

Key risk factors

Priority services

Recommended actions

Urgency

Public-welfare message

Responsible AI constraints

The AI is instructed to:

Use only supplied village data.

Not invent statistics.

Not modify calculated scores.

Distinguish calculated factors from recommendations.

Avoid claiming future flood prediction without prediction data.

Provide practical disaster-management recommendations.

🌐 Multilingual Decision Support

The dashboard supports:

🇬🇧 English

🇮🇳 Marathi

🇮🇳 Hindi

The language selector changes the dashboard interface and AI-generated assessment language.

This is intended to improve accessibility for public-sector and community-facing use cases.

📊 Analytics Dashboard

The analytics section explains why a community receives its priority.

Risk Contribution

Flood contribution

Population contribution

Service-gap contribution

River vulnerability contribution

Infrastructure Deficits

Healthcare gap

Water gap

Drainage gap

📑 Dataset Ledger

The dashboard provides a structured village-level dataset view containing:

Priority rank

Village

District

Welfare priority

Vulnerability score

Flood exposure

Hospital distance

Service-gap score

Filtered results can be exported as CSV for downstream analysis and reporting.

🏗️ System Architecture

                 ┌──────────────────────┐
                 │ GIS / Village Data   │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Data Cleaning &      │
                 │ Validation           │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Feature Engineering  │
                 └──────────┬───────────┘
                            ↓
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
       Flood Score    Population Score   Service Gaps
             └──────────────┼──────────────┘
                            ↓
                 ┌──────────────────────┐
                 │ K-Means ML           │
                 │ Vulnerability         │
                 │ Segmentation          │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Underserved Score    │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ Welfare Priority     │
                 │ Score + Ranking      │
                 └──────────┬───────────┘
                            ↓
              ┌─────────────┴─────────────┐
              ↓                           ↓
     ┌──────────────────┐       ┌──────────────────┐
     │ Interactive GIS  │       │ Gemini AI Copilot │
     │ Visualization    │       │ Recommendations  │
     └────────┬─────────┘       └────────┬─────────┘
              └─────────────┬─────────────┘
                            ↓
                 ┌────────────────────────┐
                 │ Disaster Management    │
                 │ Decision Support       │
                 └────────────────────────┘

🔄 End-to-End Workflow

Step

Process

1

Data Collection

2

Data Cleaning

3

Feature Engineering

4

ML Vulnerability Segmentation

5

Vulnerability Assessment

6

Welfare Prioritization

7

GIS Visualization

8

AI Decision Support

9

Actionable Recommendations

Feature Engineering

The system derives:

Population density

Water availability

Drainage availability

Flood score

Population score

Healthcare gap

Water gap

Drainage gap

Service gap

River vulnerability

🧰 Technology Stack

Layer

Technologies

Programming

Python

Data Processing

Pandas, NumPy

Machine Learning

Scikit-learn, K-Means, StandardScaler

Model Evaluation

Silhouette Score

GIS

Folium, GeoJSON, Streamlit-Folium

Dashboard

Streamlit

Visualization

Plotly

Generative AI

Google Gemini API, google-genai

Configuration

Python Dotenv

📁 Repository Structure

AI-GIS-FVWPS/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── external/
│   │   ├── study_area_3districts.geojson
│   │   ├── village_ai_final.geojson
│   │   ├── village_flooded_area_district.geojson
│   │   ├── river_network_in_district.geojson
│   │   ├── hospitals_3districts.geojson
│   │   └── road.geojson
│   │
│   ├── health.csv
│   ├── village_ai_ml_final.csv
│   └── village_ai_ml_health.csv
│
└── src/
    ├── __init__.py
    ├── config.py
    ├── data_loader.py
    ├── feature_engineering.py
    ├── gemini_ai.py
    ├── i18n.py
    ├── main.py
    ├── merge_health.py
    ├── vulnerability_model.py
    └── welfare_priority.py

⚙️ Installation

1. Clone the repository

git clone https://github.com/karthikeyanravikumar-ds/AI-GIS-FVWPS.git
cd AI-GIS-FVWPS

2. Create a virtual environment

Windows

python -m venv .venv
.venv\Scripts\activate

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

🔐 Gemini API Configuration

The AI Copilot requires a Gemini API key.

Create:

.env

in the project root.

Add:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

⚠️ Security

Never commit .env or expose your API key publicly.

Keep credentials in environment variables.

Ensure .env is included in .gitignore.

Never hard-code API keys.

Use proper secret management for production deployments.

▶️ Run the Prototype

Start the Streamlit application:

streamlit run app.py

Open:

http://localhost:8501

🖥️ Prototype Walkthrough

Once the dashboard opens:

1. Select Language

Choose English, Marathi, or Hindi.

2. Select District

Use the district filter to narrow the study area.

3. Select Priority

Filter communities by:

All

High

Moderate

Low

4. Select a Village

Choose a target village to inspect its assessment.

5. Explore the GIS Map

Toggle:

Flood Zones

Rivers

Hospitals

Roads

6. Inspect Risk Indicators

Review:

Flood Exposure

Vulnerability Index

Welfare Priority Score

Hospital Distance

Service Gap

7. Open Analytics

Understand the contribution of:

Flood exposure

Population

Service gaps

River vulnerability

8. Open AI Copilot

Generate a village-specific assessment and recommended actions.

9. Inspect Dataset Ledger

Review and export the filtered village-level dataset.

📌 Example Decision-Support Flow

Village
   ↓
High Flood Exposure
   ↓
High Population Exposure
   ↓
Large Hospital Distance
   ↓
Poor Water / Drainage Infrastructure
   ↓
High Service Gap
   ↓
High Welfare Priority
   ↓
Priority Services Identified
   ↓
AI-Generated Response Recommendations

The goal is to convert multiple GIS and tabular indicators into one interpretable decision-support workflow.

🔬 Technical Methodology

Normalization

Most vulnerability indicators are converted to a 0–100 scale using Min-Max normalization.

Score =
((Value - Minimum) /
 (Maximum - Minimum)) × 100

Missing values are handled through median imputation where appropriate.

Machine Learning

StandardScaler
      ↓
K-Means
      ↓
K = 2...5 Evaluation
      ↓
Silhouette Score
      ↓
Best K
      ↓
Village Clusters

🎯 Welfare Prioritization Methodology

The model is intentionally interpretable.

                 FLOOD
                  40%
                   │
                   ▼
SERVICE GAP 30% → PRIORITY ← POPULATION 20%
                   ▲
                   │
              UNDERSERVED
                  10%

The design allows decision makers to understand why a community receives a particular priority score rather than relying entirely on an opaque black-box prediction.

🤖 Responsible AI Design

Generative AI is used as a decision-support layer, not as the source of the underlying analytical calculation.

AI receives

Village information

District

Calculated vulnerability indicators

Welfare score

Service gaps

Priority services

Other supplied assessment attributes

AI produces

Risk summary

Priority explanation

Key risk factors

Recommended actions

Urgency

Public-welfare message

AI does not

Independently calculate the official vulnerability score

Modify the ML-derived priority score

Invent statistics

Claim future flood prediction without prediction data

Provide medical diagnosis

🌍 Scalability

The architecture is based on reusable village-level features.

One Village
    ↓
Multiple Villages
    ↓
Multiple Districts
    ↓
Entire State
    ↓
Multiple States
    ↓
National Disaster-Management Datasets

The modular separation of:

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

makes individual components easier to upgrade without redesigning the complete application.

📈 Future Scope

🌧️ Real-Time Flood Monitoring

Potential integrations:

Rainfall data

River-level sensors

Weather APIs

Satellite imagery

Near-real-time flood observations

🔮 Predictive Flood Modelling

Future versions could incorporate:

Rainfall forecasting

River-level prediction

Temporal flood modelling

Time-series ML

Remote-sensing-based inundation prediction

🗺️ Larger Geographic Coverage

Potential expansion:

Additional districts

Entire Maharashtra

Other Indian states

National-scale disaster-management applications

🚑 Resource Allocation Optimization

Future versions could support:

Evacuation-centre placement

Ambulance allocation

Relief-material distribution

Emergency-team deployment

Temporary healthcare facilities

📱 Mobile / Field Application

Officials or volunteers could:

Report local flooding

Upload photographs

Update infrastructure conditions

Report blocked roads

Report service outages

🧪 Prototype Scope & Limitations

This project is a hackathon prototype and decision-support system, not a certified disaster-management platform.

Current limitations:

The prototype uses prepared datasets rather than a complete real-time disaster-data infrastructure.

The ML component performs vulnerability segmentation rather than future flood forecasting.

Welfare scores depend on the quality and coverage of supplied datasets.

GIS accuracy depends on the underlying spatial datasets.

AI-generated recommendations should be reviewed by qualified authorities before operational use.

The prototype should not be interpreted as an official government risk classification.

These limitations define the boundary between the current prototype and a production disaster-management system.

🔐 Security Considerations

Store API credentials in .env.

Keep .env excluded from Git.

Never hard-code API keys.

Do not publicly commit sensitive operational datasets.

Use secret-management services for production.

Keep AI-generated recommendations subject to human review.

🧩 Design Principles

1. Explainability

Priority scores should be understandable.

2. Spatial Context

Risk should be interpreted geographically.

3. Human-Centered AI

AI should assist decision makers rather than replace them.

4. Welfare-Oriented Prioritization

The system focuses on people and essential services, not only physical flood exposure.

5. Modular Architecture

Data, ML, GIS, prioritization, and AI components remain logically separated.

🏆 Innovation

The primary innovation is the integration of multiple decision layers into a single workflow:

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

Instead of producing another static flood-risk map, the prototype aims to create a:

People-centric prioritization engine for disaster response.

🌐 Real-World Impact

Emergency resources are limited, while vulnerable communities can be numerous.

AI-GIS-FVWPS is designed to help decision makers move from:

"These areas are flooded."

to:

"These communities are most vulnerable,
these are the contributing factors,
these essential services are deficient,
and these communities should be considered
for priority intervention."

Potential stakeholders

District disaster-management authorities

Local government bodies

Emergency response teams

Public-health departments

NGOs

Relief organizations

Infrastructure planners

Community welfare organizations

🧭 Intended Users

User

Potential Use

🏛️ Government / Disaster Management

Identify and rank communities requiring attention

🚨 Emergency Response Teams

Understand spatial concentration of vulnerable communities

🏥 Public Health Authorities

Identify healthcare-access gaps

🤝 NGOs & Relief Organizations

Prioritize welfare interventions

🏗️ Urban / Rural Planners

Identify infrastructure deficits

🔬 Researchers

Experiment with AI, GIS and spatial vulnerability modelling

🧪 Suggested Hackathon Demo

Scenario

A disaster-management officer wants to identify communities requiring priority welfare intervention.

Demonstration Flow

1. Open Dashboard
        ↓
2. Select District
        ↓
3. Observe Flood Zones
        ↓
4. Select Village
        ↓
5. Review Vulnerability Score
        ↓
6. Review Flood Exposure
        ↓
7. Review Hospital Distance
        ↓
8. Review Service Gaps
        ↓
9. Review Welfare Priority
        ↓
10. Open AI Copilot
        ↓
11. Generate Recommendations
        ↓
12. Switch Language
        ↓
13. Export Dataset

This demonstrates the complete value chain rather than only showing the map.

🛠️ Troubleshooting

Streamlit command not found

Activate the virtual environment:

.venv\Scripts\activate

Then reinstall dependencies:

pip install -r requirements.txt

Gemini API Error

Verify that .env exists in the project root:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Dataset Loading Error

Verify the expected directories exist:

data/
data/external/
outputs/

The dashboard expects processed datasets and GIS layers at the paths configured by the application.

GIS Layers Not Appearing

Verify that the following files exist under data/external/:

study_area_3districts.geojson
village_ai_final.geojson
village_flooded_area_district.geojson
river_network_in_district.geojson
hospitals_3districts.geojson
road.geojson

📚 Data & Methodology Transparency

The repository contains both tabular and geospatial assets used by the prototype.

The preprocessing pipeline:

Cleans duplicate records

Removes empty columns

Standardizes missing-value representations

Converts relevant attributes to numeric form

The feature-engineering pipeline derives:

Population indicators

Water indicators

Drainage indicators

Healthcare indicators

Flood indicators

River-related indicators

These are then used within the vulnerability and welfare-prioritization pipeline.

🔭 Future Vision

AI-GIS-FVWPS is intended as a foundation for a broader:

People-Centric AI Disaster Management Platform

A mature production system could continuously combine:

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

The long-term objective is to help authorities answer three questions:

WHERE?

Where is the hazard and vulnerability concentrated?

WHO?

Which communities are most exposed and underserved?

WHAT NEXT?

What intervention should be prioritized?

👥 Team

AI-GIS-FVWPS — Team Contributions

Team Member

Role

Contribution

Karthikeyan

🗺️ GIS Mapping

GIS layers, spatial visualization, flood-zone mapping, river, hospital and road layers

Karthikeyan & Angel

🤖 ML & Scoring

Vulnerability modelling, feature analysis, ML segmentation, welfare-priority scoring and interpretation

Kishore

🖥️ Streamlit & Interface

Streamlit dashboard structure and user interface for interacting with analytical modules

📜 License

The project is intended as an open-source hackathon prototype.

Recommended license: MIT License

If MIT is selected, add a LICENSE file containing the official MIT License text before final submission.

⭐ Acknowledgement

Built as an open-source AI + GIS prototype for OOSC 4.0 — Opportunity Open Source Conference, IIIT Allahabad.

The project demonstrates how open-source geospatial technologies, machine learning, and generative AI can be combined to create practical, explainable, and people-centric disaster-management decision-support systems.

🔗 Project Links

🌐 Live Prototype: https://karthikeyanravikumar-ds-ai-gis-fvwps-app-aomepe.streamlit.app/

💻 GitHub: https://github.com/karthikeyanravikumar-ds/AI-GIS-FVWPS

🎥 Demo Video: https://youtu.be/fXOyZhNUklY

🏆 OOSC 4.0: https://oosc.iiita.ac.in/hackathon

💬 One-Line Project Pitch

AI-GIS-FVWPS transforms flood maps into actionable welfare priorities by combining geospatial risk, population exposure, essential-service gaps, machine learning, and generative AI to identify which underserved communities need attention first.

<p align="center">
  <strong>🌊 From Flood Mapping → to Vulnerability → to Priority → to Action.</strong>
</p>