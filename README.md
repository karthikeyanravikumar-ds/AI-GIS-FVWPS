<div align="center">

🛡️ AI-GIS-FVWPS

AI-GIS Flood Vulnerability & Public Welfare Prioritization System

Turning flood-risk maps into people-centric, actionable welfare priorities.






<br>

An AI + GIS decision-support prototype that identifies flood-vulnerable and underserved communities, ranks them by public-welfare priority, visualizes risk spatially, and generates practical response recommendations.

</div>

🚨 The Problem

Most flood-management systems answer one question:

“Where is the flood risk?”

But flood exposure alone does not tell us who needs help first.

Two communities can face similar flood exposure while having very different levels of:

👥 Population exposure

🏥 Healthcare accessibility

💧 Drinking-water availability

🚰 Drainage infrastructure

🛣️ Road connectivity

🌊 River proximity

🏘️ Essential-service access

📊 Overall vulnerability

Our question

Which communities are most vulnerable, why are they vulnerable, what essential services are missing, and where should limited resources be prioritized first?

💡 Our Solution

AI-GIS-FVWPS combines GIS + Machine Learning + Generative AI + public-welfare scoring into one decision-support workflow.

                  FLOOD / VILLAGE DATA
                           │
                           ▼
                ┌─────────────────────┐
                │ Data Cleaning &     │
                │ Validation          │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Feature Engineering │
                └──────────┬──────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
     Flood Risk       Population       Service Gaps
          │             Exposure        Healthcare
          │                              Water
          │                              Drainage
          └────────────────┬─────────────┘
                           ▼
                ┌─────────────────────┐
                │ K-Means Vulnerability│
                │ Segmentation         │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Underserved Score   │
                └──────────┬──────────┘
                           ▼
                ┌─────────────────────┐
                │ Welfare Priority    │
                │ Score + Ranking     │
                └──────────┬──────────┘
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
        🗺️ Interactive GIS      🧠 Gemini AI
          Visualization         Decision Support
                │                     │
                └──────────┬──────────┘
                           ▼
                🎯 ACTIONABLE PRIORITIES

In simple terms

Machine Learning calculates → GIS visualizes → Generative AI explains → Decision makers act.

⭐ Why This Project Is Different

Traditional systems often stop at:

Hazard Mapping

Our workflow continues through:

Hazard
  ↓
Vulnerability
  ↓
Service Gaps
  ↓
Underserved Communities
  ↓
Welfare Priority
  ↓
Recommended Action

The goal is not to create another static flood map.

The goal is to build a people-centric disaster decision-support layer.

🧩 Core Features

Feature

What it does

🗺️ Interactive GIS

Visualizes villages, flood zones, rivers, hospitals and roads

🌊 Flood Exposure

Converts flood exposure into a normalized 0–100 score

👥 Population Exposure

Estimates potential human impact using population density

🏥 Healthcare Gap

Uses hospital distance to identify healthcare-access vulnerability

💧 Water Gap

Evaluates available water infrastructure

🚰 Drainage Gap

Incorporates drainage infrastructure into vulnerability

🌊 River Vulnerability

Uses river proximity as a spatial risk factor

🤖 ML Segmentation

Uses K-Means to discover vulnerability groups

🏘️ Underserved Score

Identifies communities affected by service deficiencies

🎯 Welfare Priority

Ranks communities for intervention

🧠 AI Copilot

Converts calculated assessments into readable recommendations

🌐 Multilingual UI

English, Marathi and Hindi support

📊 Analytics

Explains the contribution of major risk factors

📑 Dataset Ledger

Filters and exports village-level assessment data

🗺️ Interactive GIS Command Center

The dashboard uses Folium + Streamlit for interactive geospatial analysis.

Available layers

District boundaries

Village boundaries

Flood inundation zones

River networks

Hospitals

Roads

Village priority levels

Selected village locations

Basemaps

OpenStreetMap

CartoDB Positron

Satellite imagery

Users can toggle layers, select a village, and inspect its spatial context.

🤖 Machine Learning

K-Means Vulnerability Segmentation

The ML pipeline uses:

Flood Score
Population Score
Healthcare Gap
Water Gap
Drainage Gap
River Vulnerability

Preprocessing

Convert relevant variables to numeric form.

Handle missing values using median imputation.

Standardize features using StandardScaler.

Evaluate multiple K-Means configurations.

Select the configuration with the best silhouette score.

Candidate cluster counts

K = 2
K = 3
K = 4
K = 5

This enables the system to discover groups of communities with similar vulnerability characteristics.

Important: The current ML component performs vulnerability segmentation. It is not a future flood forecasting model.

🎯 Welfare Prioritization Engine

The welfare-priority model is intentionally interpretable.

Welfare Priority Formula

Factor

Weight

🌊 Flood Vulnerability

40%

🏥 Essential Service Gap

30%

👥 Population Exposure

20%

🏘️ Underserved Condition

10%

Welfare Priority Score
=
0.40 × Flood Vulnerability
+ 0.30 × Service Gap
+ 0.20 × Population Exposure
+ 0.10 × Underserved Score

Final range:

0–100

🏘️ Underserved Community Score

Service Gap       = 50%
Population        = 30%
Flood Exposure    = 20%

Underserved Score
=
0.50 × Service Gap
+ 0.30 × Population Exposure
+ 0.20 × Flood Exposure

The score is normalized to 0–100.

This captures an important distinction:

A community can be highly vulnerable not only because of flooding, but because essential services are difficult to access.

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

The system also generates a priority rank across the study area.

🏥 From Risk to Action

The system can identify potential priority services based on service-gap indicators:

🏥 Healthcare

💧 Drinking water

🚰 Drainage

🚨 Emergency response

🚌 Evacuation support

🍱 Food supplies

🛣️ Road / connectivity

🏘️ Other public-welfare interventions

Risk
 ↓
Service Deficiency
 ↓
Priority
 ↓
Recommended Action

🧠 Gemini AI Copilot

The Generative AI layer uses Google Gemini as a decision-support assistant.

The AI does NOT calculate the official score.

Instead:

GIS + ML
   ↓
Calculated Assessment
   ↓
Gemini
   ↓
Human-Readable Explanation
   ↓
Recommended Actions

AI outputs

Risk summary

Priority explanation

Key risk factors

Priority services

Recommended actions

Urgency

Public-welfare message

Responsible AI constraints

The AI is instructed to:

Use only supplied village data

Never invent statistics

Never modify calculated scores

Separate analysis from recommendations

Avoid unsupported future flood predictions

Provide practical disaster-management recommendations

Machine Learning calculates. GIS visualizes. Generative AI explains and recommends.

🌐 Multilingual Decision Support

The dashboard supports:

🇬🇧 English
🇮🇳 Marathi
🇮🇳 Hindi

The selected language affects both the dashboard interface and AI-generated assessment.

This is designed to make the system more accessible for public-sector and community-facing scenarios.

📊 Analytics Dashboard

The analytics layer explains why a community has been prioritized.

Risk contribution

Flood contribution

Population contribution

Service-gap contribution

River vulnerability contribution

Infrastructure deficits

Healthcare gap

Water gap

Drainage gap

📑 Dataset Ledger

The dashboard provides a structured village-level assessment containing:

Priority rank

Village

District

Welfare priority

Vulnerability score

Flood exposure

Hospital distance

Service-gap score

Filtered results can be exported as CSV.

🏗️ System Architecture

┌───────────────────────────────────────────────┐
│              GIS / VILLAGE DATA               │
└───────────────────────┬───────────────────────┘
                        ▼
┌───────────────────────────────────────────────┐
│           DATA CLEANING & VALIDATION           │
└───────────────────────┬───────────────────────┘
                        ▼
┌───────────────────────────────────────────────┐
│              FEATURE ENGINEERING               │
└───────────────────────┬───────────────────────┘
                        ▼
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   FLOOD SCORE     POPULATION       SERVICE GAPS
                      SCORE
        └───────────────┼───────────────┘
                        ▼
┌───────────────────────────────────────────────┐
│       K-MEANS VULNERABILITY SEGMENTATION      │
└───────────────────────┬───────────────────────┘
                        ▼
┌───────────────────────────────────────────────┐
│             UNDERSERVED SCORE                 │
└───────────────────────┬───────────────────────┘
                        ▼
┌───────────────────────────────────────────────┐
│        WELFARE PRIORITY + RANKING             │
└───────────────────────┬───────────────────────┘
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
      ┌──────────────┐      ┌──────────────┐
      │   GIS MAP    │      │ GEMINI AI    │
      │ Visualization│      │  COPILOT     │
      └──────┬───────┘      └──────┬───────┘
             └──────────┬──────────┘
                        ▼
┌───────────────────────────────────────────────┐
│       DISASTER MANAGEMENT DECISION SUPPORT    │
└───────────────────────────────────────────────┘

🔄 End-to-End Workflow

01  Data Collection
        ↓
02  Data Cleaning
        ↓
03  Feature Engineering
        ↓
04  ML Vulnerability Segmentation
        ↓
05  Vulnerability Assessment
        ↓
06  Welfare Prioritization
        ↓
07  GIS Visualization
        ↓
08  AI Decision Support
        ↓
09  Actionable Recommendations

🧰 Technology Stack

Layer

Technology

🐍 Programming

Python

🧹 Data Processing

Pandas, NumPy

🤖 Machine Learning

Scikit-learn

🔵 Clustering

K-Means

📏 Scaling

StandardScaler

📐 Evaluation

Silhouette Score

🗺️ GIS

Folium, GeoJSON

🌍 Map Integration

Streamlit-Folium

🖥️ Dashboard

Streamlit

📊 Visualization

Plotly

🧠 Generative AI

Google Gemini API

🔌 Gemini SDK

google-genai

🔐 Configuration

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

⚙️ Getting Started

Prerequisites

Python 3.x

Git

Gemini API key for AI Copilot functionality

1. Clone

git clone https://github.com/karthikeyanravikumar-ds/AI-GIS-FVWPS.git
cd AI-GIS-FVWPS

2. Create virtual environment

Windows

python -m venv .venv
.venv\Scripts\activate

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Configure Gemini

Create .env:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Never commit .env or expose your API key.

5. Run

streamlit run app.py

Open:

http://localhost:8501

🖥️ Prototype Walkthrough

🌐 Open Dashboard
        ↓
🗺️ Select District
        ↓
🌊 Explore Flood Zones
        ↓
📍 Select Village
        ↓
📊 Review Vulnerability
        ↓
🏥 Check Hospital Distance
        ↓
💧 Review Service Gaps
        ↓
🎯 Check Welfare Priority
        ↓
🧠 Open AI Copilot
        ↓
💡 Generate Recommendations
        ↓
🌐 Switch Language
        ↓
📑 Export Dataset

Suggested hackathon demo

Show the complete journey rather than only the map:

Map → Risk → Why → Service Gap → Priority → AI Recommendation

🧪 Technical Methodology

Normalization

Most vulnerability indicators are converted to a 0–100 scale using Min-Max normalization.

Score =
((Value - Minimum) /
 (Maximum - Minimum)) × 100

ML Pipeline

Raw Features
     ↓
Median Imputation
     ↓
StandardScaler
     ↓
K-Means (K=2...5)
     ↓
Silhouette Score
     ↓
Best K
     ↓
Village Vulnerability Clusters

🌍 Real-World Impact

Emergency resources are limited, while vulnerable communities can be numerous.

AI-GIS-FVWPS aims to help decision makers move from:

“These areas are flooded.”

to:

“These communities are most vulnerable, these are the contributing factors, these essential services are deficient, and these communities should be considered for priority intervention.”

Potential stakeholders

🏛️ District disaster-management authorities

🏢 Local government bodies

🚨 Emergency response teams

🏥 Public-health departments

🤝 NGOs

📦 Relief organizations

🏗️ Infrastructure planners

🏘️ Community welfare organizations

🧭 Intended Users

User

Use Case

🏛️ Government

Rank communities requiring attention

🚨 Emergency Teams

Understand spatial vulnerability

🏥 Public Health

Identify healthcare-access gaps

🤝 NGOs

Prioritize welfare interventions

🏗️ Planners

Identify infrastructure deficits

🔬 Researchers

Experiment with AI/GIS vulnerability modelling

🏆 Innovation

The project combines:

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
     ↓
PEOPLE-CENTRIC AI-GIS
DISASTER DECISION SUPPORT

The key shift

From:

Flood Mapping

To:

Vulnerability → Priority → Action

🔐 Responsible AI & Limitations

This is a hackathon prototype, not a certified disaster-management platform.

Current limitations

Uses prepared datasets rather than a complete real-time disaster-data infrastructure.

ML performs vulnerability segmentation rather than future flood forecasting.

Welfare scores depend on dataset quality and coverage.

GIS accuracy depends on underlying spatial data.

AI recommendations require human review before operational use.

Scores should not be interpreted as official government classifications.

Security

Store API keys in .env.

Keep .env out of Git.

Never hard-code credentials.

Avoid committing sensitive operational datasets.

Use secret-management services in production.

🚀 Future Roadmap

Phase 1 — Prototype

GIS flood visualization

Village vulnerability indicators

K-Means segmentation

Welfare-priority scoring

Gemini AI Copilot

Multilingual support

Dataset export

Phase 2 — Real-Time Intelligence

Rainfall integration

River-level sensors

Weather APIs

Satellite imagery

Near-real-time flood observations

Phase 3 — Predictive Intelligence

Rainfall forecasting

River-level prediction

Temporal flood modelling

Time-series ML

Remote-sensing-based inundation prediction

Phase 4 — Operational Decision Support

Evacuation-centre optimization

Ambulance allocation

Relief-material distribution

Emergency-team deployment

Temporary healthcare facility planning

Mobile / field reporting application

Geographic expansion

Current Study Area
       ↓
Multiple Districts
       ↓
Entire Maharashtra
       ↓
Other Indian States
       ↓
National Scale

📜 Scope & Transparency

AI-GIS-FVWPS is designed as a decision-support prototype.

It does not replace:

Government disaster-management systems

Official flood warnings

Qualified disaster-management authorities

Professional emergency-response decisions

The system is intended to demonstrate how open-source GIS + ML + Generative AI can support more explainable and people-centric disaster planning.

👥 Team

Member

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

Streamlit dashboard structure and user interface

🏆 OOSC 4.0

Developed as a functional prototype for:

Opportunity Open Source Conference (OOSC) 4.0 — IIIT Allahabad

The project demonstrates how open-source technologies can be combined to create a practical, explainable and people-centric disaster-management decision-support system.

🔗 Project Links





🌐 Live Prototype

Launch App

💻 GitHub

View Repository

🎥 Demo Video

Watch Demo

🏆 OOSC 4.0

Hackathon Page

📄 License

The project is intended as an open-source hackathon prototype.

Recommended: MIT License

If selected, add the official MIT License text in a LICENSE file.

<div align="center">

💬 Project Pitch

“AI-GIS-FVWPS transforms flood maps into actionable welfare priorities by combining geospatial risk, population exposure, essential-service gaps, machine learning and generative AI to identify which underserved communities need attention first.”

<br>

🌊 Map the Risk. Understand the Vulnerability. Prioritize the People.

⭐ If you find this project useful, consider giving the repository a star!

</div>