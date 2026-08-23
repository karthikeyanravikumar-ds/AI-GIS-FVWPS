from pathlib import Path

# ---------------------------------------------------------
# SYSTEM METADATA & BRANDING
# ---------------------------------------------------------

SYSTEM_NAME = "AI-GIS FVWPS"
SYSTEM_FULL_NAME = "Flood Vulnerability & Public Welfare Prioritization System"
SYSTEM_TAGLINE = "Geospatial & Machine Learning Decision Support System"
VERSION = "1.0.0"

# ---------------------------------------------------------
# DIRECTORY PATHS
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
EXTERNAL_GIS_DIR = DATA_DIR / "external"

# ---------------------------------------------------------
# FILE PATHS
# ---------------------------------------------------------

INPUT_FILE = DATA_DIR / "village_ai_ml_health.csv"

FINAL_OUTPUT = OUTPUT_DIR / "village_ai_final.csv"
TOP_PRIORITY_OUTPUT = OUTPUT_DIR / "top_priority_villages.csv"
CLUSTER_OUTPUT = OUTPUT_DIR / "cluster_summary.csv"

GIS_FILES = {
    "study_area": EXTERNAL_GIS_DIR / "study_area_3districts.geojson",
    "villages": EXTERNAL_GIS_DIR / "village_ai_final.geojson",
    "flood": EXTERNAL_GIS_DIR / "village_flooded_area_district.geojson",
    "rivers": EXTERNAL_GIS_DIR / "river_network_in_district.geojson",
    "hospitals": EXTERNAL_GIS_DIR / "hospitals_3districts.geojson",
    "roads": EXTERNAL_GIS_DIR / "road.geojson",
}

# Ensure outputs directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------
# PRD MODEL WEIGHTS
# ---------------------------------------------------------

FLOOD_WEIGHT = 0.40
SERVICE_WEIGHT = 0.30
POPULATION_WEIGHT = 0.20
RIVER_WEIGHT = 0.10