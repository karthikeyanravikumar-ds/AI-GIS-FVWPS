import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from google import genai

# Load .env locally if present
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
if ENV_FILE.exists():
    load_dotenv(dotenv_path=ENV_FILE, override=True)

# Try Streamlit Secrets first (for Cloud), then fallback to environment variable (for Local)
API_KEY = None
if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not configured in .env or Streamlit Secrets.")

client = genai.Client(api_key=API_KEY)

# =========================================================

# SYSTEM PROMPT

# =========================================================



SYSTEM_PROMPT = """

You are an AI disaster-management decision-support assistant

for an AI-GIS based Flood Vulnerability and Public Welfare

Prioritization System for Maharashtra, India.



The system identifies underserved communities affected by floods.



Your job is to interpret already-calculated GIS and ML results.



IMPORTANT RULES:



1. Do not invent statistics.

2. Do not change the calculated vulnerability or priority score.

3. Do not claim that you predicted a future flood unless explicitly

   provided with a prediction dataset.

4. Use only the supplied village data.

5. Distinguish between observed/calculated factors and recommendations.

6. Recommendations should focus on public welfare and disaster response.

7. Consider:

   - emergency response

   - healthcare

   - evacuation

   - drinking water

   - food supplies

   - road/connectivity

   - drainage

8. Keep recommendations practical.

9. Do not provide medical diagnosis.

10. The output must be suitable for a government/disaster-management

    decision-support dashboard.

"""





# =========================================================

# GENERATE VILLAGE ASSESSMENT

# =========================================================



def generate_village_assessment(village_data, language="English"):



    prompt = f"""

{SYSTEM_PROMPT}



Analyze the following village-level assessment:



{json.dumps(village_data, indent=2, default=str)}



Generate the response in {language}.



Return ONLY valid JSON using this structure:



{{

    "village": "",

    "district": "",

    "risk_summary": "",

    "priority_reason": "",

    "key_risk_factors": [],

    "priority_services": [],

    "recommended_actions": [],

    "urgency": "",

    "public_welfare_message": ""

}}



The key risk factors must be based only on the supplied

calculated values.



The recommended actions should correspond to the actual

service gaps and flood vulnerability.

"""



    response = client.models.generate_content(

        model="gemini-3.6-flash",

        contents=prompt,

        config={

            "response_mime_type": "application/json"

        }

    )



    return response.text





# =========================================================

# PARSE GEMINI RESPONSE

# =========================================================



def parse_assessment(response_text):



    try:



        return json.loads(

            response_text

        )



    except json.JSONDecodeError:



        return {

            "error": "Gemini returned invalid JSON",

            "raw_response": response_text

        }





# =========================================================

# CREATE VILLAGE INPUT

# =========================================================



def create_village_input(row):



    data = {



        "village": row.get(

            "village",

            "Unknown"

        ),



        "district": row.get(

            "district",

            "Unknown"

        ),



        "population": row.get(

            "total_popu",

            None

        ),



        "households": row.get(

            "total_hous",

            None

        ),



        "flood_exposure_pct": row.get(

            "flood_exposure_pct",

            None

        ),



        "flood_area_km2": row.get(

            "flood_area_km2",

            None

        ),



        "hospital_distance_km": (

    None

    if pd.isna(

        row.get(

            "hospital_dist_km",

            None

        )

    )

    else row.get(

        "hospital_dist_km"

    )

),



        "flood_vulnerability_score": row.get(

            "flood_vulnerability_score",

            None

        ),



        "service_gap_score": row.get(

            "service_gap_score",

            None

        ),



        "underserved_score": row.get(

            "underserved_score",

            None

        ),



        "vulnerability_score": row.get(

            "vulnerability_score",

            None

        ),



        "vulnerability_class": row.get(

            "vulnerability_class",

            None

        ),



        "welfare_priority_score": row.get(

            "welfare_priority_score",

            None

        ),



        "welfare_priority": row.get(

            "welfare_priority",

            None

        ),



        "priority_services": row.get(

            "priority_services",

            None

        ),



        "priority_rank": row.get(

            "priority_rank",

            None

        )

    }



    return data



def generate_multilingual_assessment(village_data):



    languages = {

        "English": "English",

        "Marathi": "Marathi (मराठी)",

        "Hindi": "Hindi (हिन्दी)"

    }



    results = {}



    for key, language in languages.items():



        print(

            f"\nGenerating {key} assessment..."

        )



        response = generate_village_assessment(

            village_data,

            language=language

        )



        results[key] = parse_assessment(

            response

        )



    return results



if __name__ == "__main__":



    import pandas as pd



    from .config import FINAL_OUTPUT



    print("\nLoading ML results...")



    df = pd.read_csv(

        FINAL_OUTPUT

    )



    # -----------------------------------------------------

    # Select highest-priority village

    # -----------------------------------------------------



    village = (

        df.sort_values(

            "welfare_priority_score",

            ascending=False

        )

        .iloc[0]

    )



    village_data = create_village_input(

        village

    )



    print(

        f"\nSelected village: "

        f"{village_data['village']}"

    )



    print(

        f"District: "

        f"{village_data['district']}"

    )



    # -----------------------------------------------------

    # Generate all languages

    # -----------------------------------------------------



    results = generate_multilingual_assessment(

        village_data

    )



    # -----------------------------------------------------

    # Display

    # -----------------------------------------------------



    print("\n")

    print("=" * 70)

    print("MULTILINGUAL GEMINI AI ASSESSMENT")

    print("=" * 70)



    for language, result in results.items():



        print("\n")

        print("=" * 30)

        print(language)

        print("=" * 30)



        print(

            json.dumps(

                result,

                indent=4,

                ensure_ascii=False

            )

        ) 

