import json
import re
from pathlib import Path

import folium
from folium.plugins import Fullscreen
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from streamlit_folium import st_folium

from src.i18n import TRANSLATIONS
from src.gemini_ai import generate_village_assessment

# ============================================================
# APP CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Flood Welfare AI | Command Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
GIS_DIR = DATA_DIR / "external"

DATA_FILE = OUTPUT_DIR / "village_ai_final.csv"
GIS_FILES = {
    "study_area": GIS_DIR / "study_area_3districts.geojson",
    "villages": GIS_DIR / "village_ai_final.geojson",
    "flood": GIS_DIR / "village_flooded_area_district.geojson",
    "rivers": GIS_DIR / "river_network_in_district.geojson",
    "hospitals": GIS_DIR / "hospitals_3districts.geojson",
    "roads": GIS_DIR / "road.geojson",
}

# ============================================================
# CSS DESIGN TOKENS
# ============================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    color: #0f172a;
    background-color: #f8fafc;
}

.block-container {
    max-width: 1600px;
    padding: 1rem 1.75rem 2.5rem 1.75rem;
}

[data-testid="stSidebar"] {
    background-color: #09131f;
    border-right: 1px solid #1e293b;
}

[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] h5 {
    color: #f8fafc !important;
}

[data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
    color: #cbd5e1 !important;
}

.app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 14px 20px;
    margin-bottom: 20px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

.app-title-group h1 {
    font-size: 20px;
    font-weight: 800;
    margin: 0;
    color: #0f172a;
}

.app-title-group p {
    margin: 2px 0 0 0;
    font-size: 13px;
    color: #64748b;
}

.badge-live {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 10px;
    border-radius: 9999px;
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    color: #065f46;
    font-size: 12px;
    font-weight: 600;
}

.badge-live-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: #10b981;
}

.kpi-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px 16px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
}

.kpi-card .kpi-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #64748b;
}

.kpi-card .kpi-val {
    font-size: 26px;
    font-weight: 800;
    margin: 6px 0 2px 0;
    color: #0f172a;
}

.kpi-card .kpi-sub {
    font-size: 12px;
    color: #64748b;
    font-weight: 500;
}

.pill-priority-high {
    color: #991b1b;
    background: #fee2e2;
    border: 1px solid #fecaca;
    padding: 2px 8px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 12px;
}

.pill-priority-moderate {
    color: #92400e;
    background: #fef3c7;
    border: 1px solid #fde68a;
    padding: 2px 8px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 12px;
}

.pill-priority-low {
    color: #065f46;
    background: #d1fae5;
    border: 1px solid #a7f3d0;
    padding: 2px 8px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 12px;
}

.dashboard-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}

.card-heading {
    font-size: 15px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 4px;
}

.card-desc {
    font-size: 13px;
    color: #64748b;
    margin-bottom: 16px;
}

.ai-summary-container {
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    border-left: 4px solid #0284c7;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 14px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# DATA CACHING
# ============================================================

@st.cache_data(show_spinner=False)
def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    data = pd.read_csv(path, low_memory=False)
    numeric_cols = [
        "vulnerability_score",
        "welfare_priority_score",
        "flood_exposure_pct",
        "hospital_dist_km",
        "underserved_score",
        "service_gap_score",
        "total_popu",
        "total_hous",
        "priority_rank",
    ]
    for col in numeric_cols:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")
    return data

@st.cache_data(show_spinner=False)
def load_geojson(path: Path):
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

df = load_data(DATA_FILE)
if df.empty:
    st.error(f"Failed to load required dataset: `{DATA_FILE}`")
    st.stop()

# ============================================================
# SIDEBAR (AI-GIS FVWPS BRANDING & WORKSPACE FILTERS)
# ============================================================

with st.sidebar:
    # 1. State initialization for language selector
    if "ui_lang" not in st.session_state:
        st.session_state.ui_lang = "English"

    t = TRANSLATIONS[st.session_state.ui_lang]

    # 2. Main Branding Header (At the very top)
    st.markdown(
        f"""
        <div style="display:flex; align-items:center; gap:12px; padding: 4px 0 16px 0; border-bottom: 1px solid #1e293b; margin-bottom: 18px;">
            <div style="font-size:28px; line-height:1;">🛡️</div>
            <div>
                <div style="font-size:16px; font-weight:800; color:#f8fafc; line-height:1.2; letter-spacing:-0.01em;">
                    {t['app_title']}
                </div>
                <div style="font-size:11px; color:#94a3b8; font-weight:500; margin-top:3px; line-height:1.3;">
                    {t['app_subtitle']}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 3. Global Interface Language Selector
    st.markdown(f"##### 🌐 {t['ui_language']}")
    ui_lang = st.selectbox(
        "Language / भाषा",
        ["English", "Marathi", "Hindi"],
        index=["English", "Marathi", "Hindi"].index(st.session_state.ui_lang),
        key="ui_lang",
        label_visibility="collapsed",
    )
    t = TRANSLATIONS[ui_lang]

    st.markdown("<hr style='border-color: #1e293b; margin: 16px 0 20px 0;'>", unsafe_allow_html=True)

    # 4. Scope & District Filters
    st.markdown(f"##### {t['filter_scope']}")

    districts = [t["all_districts"]] + sorted(
        [d for d in df["district"].dropna().astype(str).unique() if d.strip()]
    )
    selected_district = st.selectbox(t["district_boundary"], districts)

    priority_options = [t["all_priorities"], "High", "Moderate", "Low"]
    selected_priority = st.selectbox(t["welfare_priority"], priority_options)

    # Cascading query filter for village dropdown
    view_df = df.copy()
    if selected_district != t["all_districts"]:
        view_df = view_df[view_df["district"].str.casefold() == selected_district.casefold()]

    if selected_priority != t["all_priorities"]:
        view_df = view_df[view_df["welfare_priority"].astype(str).str.casefold() == selected_priority.casefold()]

    village_list = sorted(view_df["village"].dropna().astype(str).unique().tolist())

    if not village_list:
        st.warning(t["no_records"])
        st.stop()

    selected_village = st.selectbox(t["target_village"], village_list)

    # 5. Pipeline Weights Info Card (Bottom)
    st.markdown("<hr style='border-color: #1e293b; margin: 24px 0 16px 0;'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="background: rgba(255,255,255,0.03); border: 1px solid #1e293b; border-radius: 8px; padding: 10px 12px; font-size: 11px; color: #94a3b8; line-height: 1.5;">
            <div style="font-weight: 700; color: #cbd5e1; margin-bottom: 2px;">⚡ System Pipeline</div>
            <div>Weights: Flood (40%) • Service (30%) • Pop (20%) • River (10%)</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# RESOLVE ACTIVE RECORD (CRITICAL: MUST BE OUTSIDE SIDEBAR)
# ============================================================

selected_rows = df[
    df["village"].astype(str).str.casefold() == str(selected_village).casefold()
]

if selected_district != t["all_districts"]:
    selected_rows = selected_rows[
        selected_rows["district"].astype(str).str.casefold() == selected_district.casefold()
    ]

if selected_rows.empty:
    selected_rows = df[
        df["village"].astype(str).str.casefold() == str(selected_village).casefold()
    ]

active_record = selected_rows.iloc[0]



# ============================================================
# APP HEADER
# ============================================================

raw_p = str(active_record.get("welfare_priority", "Moderate")).lower()
p_badge_class = (
    "pill-priority-high" if raw_p == "high" 
    else "pill-priority-moderate" if raw_p == "moderate" 
    else "pill-priority-low"
)
priority_label = (
    t["priority_high"] if raw_p == "high"
    else t["priority_moderate"] if raw_p == "moderate"
    else t["priority_low"]
)

st.markdown(
    f"""
    <div class="app-header">
        <div class="app-title-group">
            <h1>{active_record.get('village', 'Unknown')} <span class="{p_badge_class}">{priority_label}</span></h1>
            <p>{active_record.get('district', 'Maharashtra')} &nbsp;|&nbsp; {t['rank_prefix']} <b>#{int(active_record.get('priority_rank', 0))}</b> {t['in_target_region']}</p>
        </div>
        <div class="badge-live">
            <div class="badge-live-dot"></div> {t['live_status']}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# KPI METRIC ROW
# ============================================================

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{t['kpi_flood_exp']}</div>
            <div class="kpi-val" style="color: {'#dc2626' if (active_record.get('flood_exposure_pct', 0) or 0) > 5 else '#0f172a'};">
                {active_record.get('flood_exposure_pct', 0):.1f}%
            </div>
            <div class="kpi-sub">{t['kpi_flood_sub']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{t['kpi_vuln_idx']}</div>
            <div class="kpi-val">{active_record.get('vulnerability_score', 0):.1f}</div>
            <div class="kpi-sub">{t['kpi_vuln_sub']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{t['kpi_welfare_score']}</div>
            <div class="kpi-val">{active_record.get('welfare_priority_score', 0):.1f}</div>
            <div class="kpi-sub">{t['kpi_welfare_sub']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{t['kpi_hospital_dist']}</div>
            <div class="kpi-val" style="color: {'#dc2626' if (active_record.get('hospital_dist_km', 0) or 0) > 15 else '#0f172a'};">
                {active_record.get('hospital_dist_km', 0):.1f} <span style="font-size:16px;">km</span>
            </div>
            <div class="kpi-sub">{t['kpi_hospital_sub']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k5:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{t['kpi_service_gap']}</div>
            <div class="kpi-val">{active_record.get('service_gap_score', 0):.1f}</div>
            <div class="kpi-sub">{t['kpi_service_sub']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# ============================================================
# TABS
# ============================================================

tab_map, tab_analytics, tab_copilot, tab_dataset = st.tabs(
    [
        t["tab_map"],
        t["tab_analytics"],
        t["tab_copilot"],
        t["tab_dataset"],
    ]
)

def get_feature_centroid(feature):
    """Calculates [lat, lon] center for any GeoJSON geometry safely."""
    if not isinstance(feature, dict):
        return [20.10, 79.30]

    geom = feature.get("geometry")
    if not geom or not isinstance(geom, dict):
        return [20.10, 79.30]

    raw_coords = geom.get("coordinates", [])
    coords = []

    def walk(x):
        if isinstance(x, (list, tuple)):
            if len(x) >= 2 and all(isinstance(v, (int, float)) for v in x[:2]):
                coords.append((float(x[0]), float(x[1])))
            else:
                for item in x:
                    walk(item)

    walk(raw_coords)
    
    if not coords:
        return [20.10, 79.30]

    avg_lon = sum(c[0] for c in coords) / len(coords)
    avg_lat = sum(c[1] for c in coords) / len(coords)
    return [avg_lat, avg_lon]

# ============================================================
# TAB 1: INTERACTIVE GIS OPERATIONS MAP
# ============================================================

with tab_map:
    map_ctrl_col, map_view_col = st.columns([1, 3.5])

    with map_ctrl_col:
        st.markdown(
            f"""
            <div class="dashboard-card" style="padding:14px;">
                <div class="card-heading">{t['layer_control']}</div>
                <div class="card-desc">{t['layer_desc']}</div>
            """,
            unsafe_allow_html=True,
        )
        basemap_style = st.selectbox(
            "Basemap Style",
            ["CartoDB Positron", "OpenStreetMap", "Satellite (Esri)"]
        )
        show_flood = st.checkbox(t["layer_flood"], value=True)
        show_rivers = st.checkbox(t["layer_rivers"], value=True)
        show_hospitals = st.checkbox(t["layer_hospitals"], value=True)
        show_roads = st.checkbox(t["layer_roads"], value=False)
        st.markdown("</div>", unsafe_allow_html=True)

    # 1. Determine Initial Map Center & Zoom based on Selected Village
    villages_geojson = load_geojson(GIS_FILES["villages"])
    map_center = [20.10, 79.30]
    map_zoom = 8

    selected_feature = None
    if villages_geojson:
        for feat in villages_geojson.get("features", []):
            p_name = feat.get("properties", {}).get("village", "")
            if str(p_name).casefold() == str(selected_village).casefold():
                selected_feature = feat
                map_center = get_feature_centroid(feat)
                map_zoom = 12  # Auto-zoom in on the selected village
                break

    # 2. Build Folium Map
    tile_dict = {
        "CartoDB Positron": "CartoDB positron",
        "OpenStreetMap": "OpenStreetMap",
        "Satellite (Esri)": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    }
    
    attr = "Esri World Imagery" if basemap_style == "Satellite (Esri)" else None
    
    m = folium.Map(
        location=map_center,
        zoom_start=map_zoom,
        tiles=tile_dict[basemap_style],
        attr=attr,
        control_scale=True,
        prefer_canvas=True,
    )
    Fullscreen().add_to(m)

    # 3. Add Study Area Boundary
    study_geojson = load_geojson(GIS_FILES["study_area"])
    if study_geojson:
        folium.GeoJson(
            study_geojson,
            name="District Boundaries",
            style_function=lambda x: {
                "fillColor": "#0284c7",
                "fillOpacity": 0.02,
                "color": "#334155",
                "weight": 1.8,
            },
        ).add_to(m)

    # 4. Add Roads
    if show_roads:
        roads_geojson = load_geojson(GIS_FILES["roads"])
        if roads_geojson:
            folium.GeoJson(
                roads_geojson,
                name="Roads",
                style_function=lambda x: {"color": "#64748b", "weight": 1.0, "opacity": 0.5},
            ).add_to(m)

    # 5. Add Rivers
    if show_rivers:
        rivers_geojson = load_geojson(GIS_FILES["rivers"])
        if rivers_geojson:
            folium.GeoJson(
                rivers_geojson,
                name="Rivers",
                style_function=lambda x: {"color": "#0284c7", "weight": 2.2, "opacity": 0.85},
            ).add_to(m)

    # 6. Add Flood Inundation Zones
    if show_flood:
        flood_geojson = load_geojson(GIS_FILES["flood"])
        if flood_geojson:
            folium.GeoJson(
                flood_geojson,
                name="Inundation Zones",
                style_function=lambda x: {
                    "fillColor": "#ef4444",
                    "color": "#991b1b",
                    "weight": 0.6,
                    "fillOpacity": 0.45,
                },
            ).add_to(m)

    # 7. Add Assessed Villages with Dynamic Styling and Hover Highlights
    if villages_geojson:
        def village_styler(feat):
            props = feat.get("properties", {})
            v_name = props.get("village", "")
            is_active = (v_name.casefold() == str(selected_village).casefold())
            rank = props.get("priority_rank", 999)
            
            # Highlight selected village with distinctive cyan ring
            if is_active:
                return {
                    "fillColor": "#06b6d4",
                    "color": "#0891b2",
                    "weight": 3.5,
                    "fillOpacity": 0.85,
                }
            
            # High priority (Top 10)
            if rank <= 10:
                return {
                    "fillColor": "#dc2626",
                    "color": "#991b1b",
                    "weight": 1.5,
                    "fillOpacity": 0.65,
                }
            # Moderate/Low priority
            return {
                "fillColor": "#f59e0b" if rank <= 30 else "#10b981",
                "color": "#b45309" if rank <= 30 else "#047857",
                "weight": 0.8,
                "fillOpacity": 0.4,
            }

        folium.GeoJson(
            villages_geojson,
            name="Assessed Villages",
            style_function=village_styler,
            highlight_function=lambda x: {
                "weight": 3,
                "color": "#ffffff",
                "fillOpacity": 0.9,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=["village", "district", "welfare_priority", "flood_exposure_pct", "vulnerability_score"],
                aliases=["Village:", "District:", "Priority:", "Flood Exposure (%):", "Vulnerability Score:"],
                localize=True,
                sticky=True,
            ),
            popup=folium.GeoJsonPopup(
                fields=["village", "district", "welfare_priority", "hospital_dist_km", "service_gap_score"],
                aliases=["Village", "District", "Priority Level", "Hospital Dist (km)", "Service Deficit"],
                localize=True,
            ),
        ).add_to(m)

    # 8. Add Hospitals
    if show_hospitals:
        hospitals_geojson = load_geojson(GIS_FILES["hospitals"])
        if hospitals_geojson:
            for f in hospitals_geojson.get("features", []):
                geom = f.get("geometry", {})
                if geom.get("type") == "Point":
                    coords = geom.get("coordinates", [])
                    h_name = f.get("properties", {}).get("name", "Hospital")
                    folium.CircleMarker(
                        location=[coords[1], coords[0]],
                        radius=5,
                        color="#dc2626",
                        fill=True,
                        fillColor="#fee2e2",
                        fillOpacity=0.95,
                        tooltip=f"🏥 {h_name}",
                    ).add_to(m)

    with map_view_col:
        # Returned objects capture map click events for interactive two-way binding
        map_output = st_folium(
            m,
            width=None,
            height=580,
            returned_objects=["last_active_drawing"],
        )

# ============================================================
# TAB 2: RISK & SERVICES ANALYTICS
# ============================================================

with tab_analytics:
    left_c, right_c = st.columns(2)

    with left_c:
        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="card-heading">{t['contrib_heading']}</div>
                <div class="card-desc">{t['contrib_desc']}</div>
            """,
            unsafe_allow_html=True,
        )

        contrib_factors = {
            t["factor_flood"]: active_record.get("flood_score_contribution", 35.0),
            t["factor_pop"]: active_record.get("population_score_contribution", 20.0),
            t["factor_service"]: active_record.get("service_gap_score_contribution", 25.0),
            t["factor_river"]: active_record.get("river_vulnerability_score_contribution", 20.0),
        }

        fig = go.Figure(
            go.Bar(
                x=list(contrib_factors.values()),
                y=list(contrib_factors.keys()),
                orientation="h",
                marker=dict(color="#0284c7"),
                text=[f"{v:.1f}%" for v in contrib_factors.values()],
                textposition="outside",
            )
        )
        fig.update_layout(
            height=240,
            margin=dict(l=10, r=40, t=10, b=10),
            xaxis=dict(showgrid=True, zeroline=False, gridcolor="#f1f5f9"),
            yaxis=dict(autorange="reversed"),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Plus Jakarta Sans", color="#475569", size=12),
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
        st.markdown("</div>", unsafe_allow_html=True)

    with right_c:
        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="card-heading">{t['infra_heading']}</div>
                <div class="card-desc">{t['infra_desc']}</div>
            """,
            unsafe_allow_html=True,
        )

        deficits = [
            (t["gap_health"], active_record.get("healthcare_gap_score", 0)),
            (t["gap_water"], active_record.get("water_gap_score", 0)),
            (t["gap_drainage"], active_record.get("drainage_gap_score", 0)),
        ]

        for label, val in deficits:
            clean_v = float(val or 0)
            st.markdown(f"**{label}** &nbsp;•&nbsp; `{clean_v:.1f}/100`")
            st.progress(min(max(clean_v / 100.0, 0.0), 1.0))

        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# TAB 3: AI COPILOT
# ============================================================

with tab_copilot:
    st.markdown(
        f"""
        <div class="dashboard-card">
            <div class="card-heading">{t['ai_heading']} ({ui_lang})</div>
            <div class="card-desc">{t['ai_desc']}</div>
        """,
        unsafe_allow_html=True,
    )

    cache_key = (
        str(active_record.get("village")),
        str(active_record.get("district")),
        ui_lang,
    )

    if "ai_data" not in st.session_state or st.session_state.get("ai_cache_key") != cache_key:
        st.session_state.ai_data = None

    if st.button(t["ai_btn"], type="primary"):
        with st.spinner(t["ai_spinner"]):
            try:
                payload = active_record.to_dict()
                result_json = generate_village_assessment(payload, language=ui_lang)
                st.session_state.ai_data = json.loads(result_json) if isinstance(result_json, str) else result_json
                st.session_state.ai_cache_key = cache_key
            except Exception as e:
                st.error(f"Failed to generate assessment: {e}")

    if st.session_state.ai_data:
        ai_res = st.session_state.ai_data
        st.markdown(
            f"""
            <div class="ai-summary-container">
                <div style="font-weight:700; color:#0369a1; margin-bottom:6px;">⚠️ {t['ai_urgency']} — {ai_res.get('urgency', 'High')}</div>
                <div style="font-size:14px; line-height:1.6; color:#0f172a;">
                    {ai_res.get('risk_summary', '')}
                </div>
                <div style="margin-top:10px; font-size:13px; color:#475569;">
                    <b>{ai_res.get('priority_reason', '')}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col_rf, col_act = st.columns(2)
        with col_rf:
            st.markdown(f"##### {t['ai_factors_title']}")
            for item in ai_res.get("key_risk_factors", []):
                st.warning(item, icon="📌")

        with col_act:
            st.markdown(f"##### {t['ai_tactical_title']}")
            for item in ai_res.get("recommended_actions", []):
                st.info(item, icon="🚨")

    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# TAB 4: DATASET LEDGER
# ============================================================

with tab_dataset:
    st.markdown(
        f"""
        <div class="dashboard-card">
            <div class="card-heading">{t['ledger_heading']}</div>
            <div class="card-desc">{t['ledger_desc']}</div>
        """,
        unsafe_allow_html=True,
    )

    display_cols = [
        "priority_rank",
        "village",
        "district",
        "welfare_priority",
        "vulnerability_score",
        "flood_exposure_pct",
        "hospital_dist_km",
        "service_gap_score",
    ]
    existing_cols = [c for c in display_cols if c in df.columns]

    st.dataframe(
        view_df[existing_cols].sort_values("priority_rank", ascending=True),
        use_container_width=True,
        hide_index=True,
    )

    st.download_button(
        label=t["export_btn"],
        data=view_df.to_csv(index=False).encode("utf-8"),
        file_name=f"welfare_prioritization_{ui_lang.lower()}.csv",
        mime="text/csv",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Add Base Village GeoJSON Layer
    if villages_geojson:
        def base_village_styler(feat):
            props = feat.get("properties", {}) or {}
            rank = props.get("priority_rank", 999)
            
            # High priority (Top 10)
            if rank <= 10:
                return {
                    "fillColor": "#dc2626",
                    "color": "#991b1b",
                    "weight": 1.2,
                    "fillOpacity": 0.35,
                }
            # Moderate / Lower priority
            return {
                "fillColor": "#f59e0b" if rank <= 30 else "#64748b",
                "color": "#b45309" if rank <= 30 else "#475569",
                "weight": 0.6,
                "fillOpacity": 0.20,
            }

        folium.GeoJson(
            villages_geojson,
            name="Assessed Villages",
            style_function=base_village_styler,
            highlight_function=lambda x: {
                "weight": 2.5,
                "color": "#ffffff",
                "fillOpacity": 0.7,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=["village", "district", "welfare_priority", "flood_exposure_pct", "vulnerability_score"],
                aliases=["Village:", "District:", "Priority:", "Flood Exposure (%):", "Vulnerability Score:"],
                localize=True,
                sticky=True,
            ),
        ).add_to(m)

        # ----------------------------------------------------
        # 6. DEDICATED HIGHLIGHT LAYER FOR TARGETED VILLAGE
        # ----------------------------------------------------
        if selected_feature:
            # Render highlighted polygon on top
            folium.GeoJson(
                selected_feature,
                name="Targeted Village Boundary",
                style_function=lambda x: {
                    "fillColor": "#06b6d4",
                    "color": "#0891b2",
                    "weight": 4.5,
                    "fillOpacity": 0.75,
                    "dashArray": "2, 4",
                },
                tooltip=folium.Tooltip(
                    f"🎯 <b>TARGET VILLAGE:</b> {selected_village}",
                    sticky=True,
                ),
            ).add_to(m)

            # Center Target Beacon Marker
            folium.CircleMarker(
                location=map_center,
                radius=9,
                color="#ffffff",
                weight=3,
                fill=True,
                fillColor="#0891b2",
                fillOpacity=1.0,
                popup=folium.Popup(f"<b>🎯 Selected Village:</b> {selected_village}", max_width=200),
            ).add_to(m)
