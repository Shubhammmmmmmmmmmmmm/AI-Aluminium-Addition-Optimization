# from turtle import pd
# import pandas as pd
# import streamlit as st
# from utils.prediction import predict_heat
# from utils.recommendation import generate_recommendation
# from folder.components.heat_selector import heat_selector
# df = pd.read_csv("clean_data/clean_dataset.csv")
# def digital_twin_panel(recommendation):
#     # selected_heat =  heat_selector(df)

#     # predicted = predict_heat(selected_heat)

#     # recommendation = generate_recommendation(predicted)

#     st.subheader("🏭 Digital Twin - Live Process")

#     c1, c2, c3, c4 = st.columns(4)

#     with c1:
#         st.metric(
#             "🌡 Temperature",
#             "1612 °C",
#             "+3°C"
#         )

#     with c2:
#         st.metric(
#             "🧪 Oxygen",
#             "28 ppm",
#             "-6 ppm"
#         )

#     with c3:
#         st.metric(
#             "🤖 AI Prediction",
#             "224 kg",
#             "-18 kg"
#         )

#     with c4:
#         st.metric(
#             "Recovery",
#             "93 %",
#             "+2%"
#         )

#     st.markdown("---")

#     st.markdown(f"""

# <div style="
# background:#111827;
# border-radius:18px;
# padding:20px;
# border:2px solid #2563EB;
# box-shadow:0px 6px 18px rgba(0,0,0,.4);
# ">

# <h2 style="color:#38BDF8;text-align:center;">

# 🏭 DIGITAL TWIN OF LRF

# </h2>

# <hr>

# <div style="display:flex;
# justify-content:space-between;
# align-items:center;
# font-size:20px;
# font-weight:bold;
# color:white;">

# <div style="text-align:center;width:16%;">
# 🔥<br>EAF
# </div>

# <div style="font-size:34px;color:#38BDF8;">
# ➡️
# </div>

# <div style="text-align:center;width:16%;">
# 🪣<br>LADLE
# </div>

# <div style="font-size:34px;color:#38BDF8;">
# ➡️
# </div>

# <div style="text-align:center;width:16%;">
# 💨<br>ARGON
# </div>

# <div style="font-size:34px;color:#38BDF8;">
# ➡️
# </div>

# <div style="text-align:center;width:16%;">
# 🤖<br>AI
# </div>

# <div style="font-size:34px;color:#38BDF8;">
# ➡️
# </div>

# <div style="text-align:center;width:16%;">
# 🏭<br>LRF
# </div>

# </div>

# <br>

# <div style="
# background:#172554;
# padding:15px;
# border-radius:12px;
# ">

# <h4 style="color:white;">Current AI Decision</h4>

# <ul style="color:#CBD5E1;font-size:16px;">

# <li>Al Ingot : <b style="color:#22C55E;">{recommendation["Ingot"]}</b></li>

# <li>Al Shots : <b style="color:#22C55E;">{recommendation["Shots"]} </b></li>

# <li>Al Wire : <b style="color:#22C55E;">{recommendation["Wire"]}</b></li>

# <li>Predicted Aluminum : <b style="color:#38BDF8;">{recommendation["Predicted_Al"]}</b></li>

# <li>Expected Recovery : <b style="color:#FACC15;">{recommendation["Recovery"]}</b></li>

# </ul>

# </div>

# </div>

# """, unsafe_allow_html=True)
#     st.markdown("---")

#     left, right = st.columns(2)

#     with left:

#      st.info("""
# ### Process Status

# ✅ Slag : Reducing

# ✅ Temperature : Stable

# ✅ Argon Stirring : Normal

# ✅ Heat Ready

# """)

#     with right:

#      st.success("""
# ### AI Recommendation

# ✔ Reduce Wire by 12 kg

# ✔ Do not add Al Shots

# ✔ Maintain Slag Basicity

# ✔ Send Heat to Caster

# """)
#     st.markdown("---")

#     st.progress(0.82)

#     st.caption("Digital Twin Health : 82 %")


############@2nd time#############
import streamlit as st
import pandas as pd
import textwrap
import os
import base64
import glob
import shutil
from datetime import datetime
# Set Streamlit Page Configuration
st.set_page_config(
    page_title="LRF Control Centre",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ============================================
# Asset Sync Logic
# ============================================
def sync_assets():
    assets_dir = r"assets"
    os.makedirs(assets_dir, exist_ok=True)
    
    image_mapping = {
        "eaf_furnace": "eaf_furnace.jpg",
        "ladle_pouring": "ladle_pouring.jpg",
        "argon_stirring": "argon_stirring.jpg",
        "ai_engine": "ai_engine.jpg",
        "lrf_station": "lrf_station.jpg",
        "central_ladle": "central_ladle.jpg"
    }
    
    search_dirs = [
        r"C:\Users\sK559\.gemini\antigravity\brain\844cbf76-da9e-43dd-9be8-150fe72afc8a",
        r"C:\Users\sK559\.gemini\antigravity\brain"
    ]
    
    for prefix, dest_name in image_mapping.items():
        dest_path = os.path.join(assets_dir, dest_name)
        if not os.path.exists(dest_path):
            for s_dir in search_dirs:
                if not os.path.exists(s_dir):
                    continue
                pattern = os.path.join(s_dir, f"**/{prefix}*.jpg")
                matches = glob.glob(pattern, recursive=True)
                if not matches:
                    pattern = os.path.join(s_dir, f"{prefix}*.jpg")
                    matches = glob.glob(pattern)
                if matches:
                    matches.sort(key=os.path.getmtime)
                    try:
                        shutil.copy2(matches[-1], dest_path)
                        break
                    except Exception:
                        pass
sync_assets()
# Helper to load image as base64
def get_base64_image(image_path, prefix=""):
    if os.path.exists(image_path):
        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
                return f"data:image/jpeg;base64,{encoded_string}"
        except Exception:
            pass
    # Dark high-tech SVG placeholder if file not found
    svg_placeholder = (
        f'<svg width="150" height="150" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="100%" height="100%" fill="url(#grad)" />'
        f'<defs><linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">'
        f'<stop offset="0%" style="stop-color:#0f1c3f;stop-opacity:1" />'
        f'<stop offset="100%" style="stop-color:#050b18;stop-opacity:1" />'
        f'</linearGradient></defs>'
        f'<text x="50%" y="50%" fill="#00E5FF" font-family="Segoe UI, Arial" font-size="12" '
        f'font-weight="bold" text-anchor="middle" dominant-baseline="middle">{prefix.upper()}</text>'
        f'</svg>'
    )
    encoded_string = base64.b64encode(svg_placeholder.encode()).decode()
    return f"data:image/svg+xml;base64,{encoded_string}"
# ============================================
# Load Dataset
# ============================================
def load_data():
    csv_path = "clean_data/clean_dataset.csv"
    if os.path.exists(csv_path):
        try:
            return pd.read_csv(csv_path), False
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
            return pd.DataFrame(), False
    else:
        import numpy as np
        np.random.seed(42)
        n_heats = 582
        simulated_df = pd.DataFrame({
            "Total_Al_LRF_kg": np.random.normal(loc=260, scale=55, size=n_heats),
            "LIFTING TEMP_LRF": np.random.normal(loc=1608, scale=20, size=n_heats)
        })
        return simulated_df, True
df, is_simulated = load_data()
# ============================================================
# CSS DESIGN SYSTEMS (SHARED AND DEDICATED)
# ============================================================
GLOBAL_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    /* Global Background and Typography Overrides */
    [data-testid="stAppViewContainer"] {
        background-color: #060b19 !important;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stHeader"] {
        background-color: rgba(6, 11, 25, 0.8) !important;
        backdrop-filter: blur(10px);
    }
    [data-testid="stSidebar"] {
        background-color: #0c142c !important;
    }
    
    /* Layout formatting spacing */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Common cyber elements */
    .glow-text-blue {
        color: #00E5FF;
        text-shadow: 0 0 10px rgba(0, 229, 255, 0.6);
        font-weight: 800;
    }
    
    /* Process Flow nodes animation */
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    @keyframes pulse-arrow {
        0%, 100% { transform: scale(1); opacity: 0.7; }
        50% { transform: scale(1.18); opacity: 1; }
    }
</style>
"""
# ============================================================
# PAGE 1: MANAGEMENT DASHBOARD
# ============================================================
def management_dashboard():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    st.markdown(textwrap.dedent("""
    <div style="padding-bottom:10px;">
        <h1 style="color:white; font-size:42px; font-weight:700; margin-bottom:0;">
        📊 Management Dashboard
        </h1>
        <div style="color:#AFC7E8; font-size:16px; margin-top:4px;">
        Executive dashboard for monitoring aluminium consumption,
        AI performance and estimated plant savings.
        </div>
    </div>
    """), unsafe_allow_html=True)
    st.markdown("---")
    if is_simulated:
        st.warning(
            "⚠️ CSV file `'clean_data/clean_dataset.csv'` was not found. "
            "Showing simulated placeholder data instead. Please place your CSV file in the expected path to view real plant metrics."
        )
    if df.empty:
        st.info("No data available. Please check the dataset.")
        return
    # Calculations
    total_heats = len(df)
    total_al = df["Total_Al_LRF_kg"].sum()
    avg_al = df["Total_Al_LRF_kg"].mean()
    avg_temp = df["LIFTING TEMP_LRF"].mean()
    estimated_saving = total_heats * 18
    # KPI Layout
    c1, c2, c3, c4 = st.columns(4)
    card_style = """
        background:#182744;
        border:1px solid rgba(0,229,255,.25);
        border-radius:16px;
        padding:18px;
        box-shadow: 0 0 18px rgba(0,229,255,.08);
        height:145px;
    """
    title_style = """
        color:#AFC7E8; font-size:15px; font-weight:600; margin-bottom:15px;
    """
    value_style = """
        color:#7FE7FF; font-size:40px; font-weight:700; text-shadow:0 0 10px rgba(0,229,255,.25);
    """
    with c1:
        st.markdown(textwrap.dedent(f"""
        <div style="{card_style}">
            <div style="{title_style}">🔥 Total Heats</div>
            <div style="{value_style}">{total_heats:,}</div>
        </div>
        """), unsafe_allow_html=True)
    with c2:
        st.markdown(textwrap.dedent(f"""
        <div style="{card_style}">
            <div style="{title_style}">⚙ Total Aluminium</div>
            <div style="{value_style}">{total_al:,.0f}</div>
            <div style="color:#9DB6D7;">kg</div>
        </div>
        """), unsafe_allow_html=True)
    with c3:
        st.markdown(textwrap.dedent(f"""
        <div style="{card_style}">
            <div style="{title_style}">📈 Average / Heat</div>
            <div style="{value_style}">{avg_al:.1f}</div>
            <div style="color:#9DB6D7;">kg</div>
        </div>
        """), unsafe_allow_html=True)
    with c4:
        st.markdown(textwrap.dedent(f"""
        <div style="{card_style}">
            <div style="{title_style}">🌡 Average Temperature</div>
            <div style="{value_style}">{avg_temp:.0f}</div>
            <div style="color:#9DB6D7;">°C</div>
        </div>
        """), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    # AI Model Performance
    st.markdown(textwrap.dedent("""
    <h2 style="color:white; font-weight:700;">🤖 AI Model Performance</h2>
    """), unsafe_allow_html=True)
    a1, a2, a3, a4 = st.columns(4)
    def metric_card(title, value, color="#7FE7FF"):
        st.markdown(textwrap.dedent(f"""
        <div style="
        background:#182744;
        border:1px solid rgba(0,229,255,.20);
        border-radius:15px;
        padding:18px;
        height:130px;">
            <div style="color:#AFC7E8; font-size:15px; font-weight:600;">{title}</div>
            <div style="color:{color}; font-size:38px; font-weight:700; margin-top:14px;">{value}</div>
        </div>
        """), unsafe_allow_html=True)
    with a1:
        metric_card("R² Score", "0.69")
    with a2:
        metric_card("MAE", "40 kg")
    with a3:
        metric_card("RMSE", "55 kg")
    with a4:
        metric_card("Prediction Confidence", "94%", "#00FF99")
    st.markdown("<br>", unsafe_allow_html=True)
    # Savings
    st.markdown(textwrap.dedent("""
    <h2 style="color:white; font-weight:700;">💰 Estimated Cost Saving</h2>
    """), unsafe_allow_html=True)
    p1, p2 = st.columns(2)
    with p1:
        ingot_price = st.number_input("Al Ingot Price (₹/kg)", value=410.0, step=5.0)
    with p2:
        wire_price = st.number_input("Al Wire Price (₹/kg)", value=440.0, step=5.0)
    saving_per_heat = 18
    saving_rupees = saving_per_heat * ingot_price
    monthly = saving_rupees * 250
    yearly = monthly * 12
    s1, s2, s3 = st.columns(3)
    with s1:
        metric_card("Saving / Heat", f"₹ {saving_rupees:,.0f}", "#00FF99")
    with s2:
        metric_card("Monthly Saving", f"₹ {monthly:,.0f}", "#00FF99")
    with s3:
        metric_card("Annual Saving", f"₹ {yearly:,.0f}", "#00FF99")
    st.markdown("<br>", unsafe_allow_html=True)
    # Status
    st.markdown(textwrap.dedent("""
    <h2 style="color:white; font-weight:700;">🏭 Plant AI Status</h2>
    """), unsafe_allow_html=True)
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        metric_card("AI Model", "Extra Trees", "#00E5FF")
    with k2:
        metric_card("System Status", "ONLINE", "#00FF99")
    with k3:
        metric_card("Dataset Size", f"{total_heats:,}", "#7FE7FF")
    with k4:
        metric_card("Saving Potential", f"{estimated_saving:.0f} kg", "#FFD54F")
    st.markdown("<br>", unsafe_allow_html=True)
    # Executive Summary
    st.markdown(textwrap.dedent("""
    <h2 style="color:white; font-weight:700;">📄 Executive Summary</h2>
    """), unsafe_allow_html=True)
    st.markdown(textwrap.dedent(f"""
    <div style="
        background:#17334A;
        border-left:6px solid #00FF99;
        border-radius:16px;
        padding:28px;
        box-shadow:0 0 18px rgba(0,255,153,.10);
    ">
        <h3 style="color:#00FF99; margin-top:0; margin-bottom:20px;">
            Plant Performance Overview
        </h3>
        <table style="width:100%; border-collapse:collapse;">
            <tr>
                <td style="padding:8px; color:#DCEBFF;">🔥 Total Heats Processed</td>
                <td style="padding:8px; color:#7FE7FF; font-weight:bold;">{total_heats:,}</td>
            </tr>
            <tr>
                <td style="padding:8px; color:#DCEBFF;">⚙ Total Aluminium Consumption</td>
                <td style="padding:8px; color:#7FE7FF; font-weight:bold;">{total_al:,.0f} kg</td>
            </tr>
            <tr>
                <td style="padding:8px; color:#DCEBFF;">📈 Average Aluminium / Heat</td>
                <td style="padding:8px; color:#7FE7FF; font-weight:bold;">{avg_al:.1f} kg</td>
            </tr>
            <tr>
                <td style="padding:8px; color:#DCEBFF;">💰 Estimated Saving Potential</td>
                <td style="padding:8px; color:#00FF99; font-weight:bold;">₹ {yearly:,.0f} / Year</td>
            </tr>
        </table>
        <hr style="border:1px solid rgba(255,255,255,.12); margin-top:22px; margin-bottom:18px;">
        <h4 style="color:white; margin-bottom:10px;">AI Recommendations</h4>
        <div style="color:#DCEBFF; line-height:2;">
            ✅ Continue AI-Based Aluminium Prediction<br>
            ✅ Maintain Reducing Slag Practice<br>
            ✅ Monitor Oxygen Before Final Aluminium Addition<br>
            ✅ Maintain Proper Argon Stirring Practice<br>
            ✅ Expected Recovery : <span style="color:#00FF99;">92%</span><br>
            ✅ AI Prediction Confidence : <span style="color:#00FF99;">94%</span>
        </div>
    </div>
    """), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("📌 Management Dashboard provides an executive overview of plant performance, aluminium consumption, AI model health and estimated cost savings.")
# ============================================================
# PAGE 2: DIGITAL TWIN OF LRF
# ============================================================
def digital_twin_dashboard(heat_id, grade, temperature_val, oxygen_val, basicity_val, feo_val, c_val, mn_val, si_val, n_val, health_val):
    # Dynamic calculations
    time_now = datetime.now()
    time_str = time_now.strftime("%H:%M:%S")
    date_str = time_now.strftime("%d %b %Y")
    
    # Delta calculations
    temp_delta = temperature_val - 1609
    temp_sign = "+" if temp_delta >= 0 else ""
    temp_color = "#ff5252" if temperature_val > 1650 or temperature_val < 1590 else "#00FF99"
    temp_arrow = "▲" if temp_delta >= 0 else "▼"
    
    oxy_delta = oxygen_val - 34
    oxy_sign = "+" if oxy_delta >= 0 else ""
    oxy_arrow = "▲" if oxy_delta >= 0 else "▼"
    oxy_color = "#ff5252" if oxygen_val > 45 else "#00FF99" # high oxygen is bad
    
    # Calculate AI prediction based on sensors
    predicted_al = int(max(100, 224 + (oxygen_val - 28) * 1.8 - (temperature_val - 1612) * 1.2))
    pred_delta = predicted_al - 242
    pred_sign = "+" if pred_delta >= 0 else ""
    pred_arrow = "▲" if pred_delta >= 0 else "▼"
    
    # Calculate recovery based on slag parameters
    rec_val = min(98, max(80, int(93 + (basicity_val - 2.92) * 4 - (feo_val - 8.6) * 0.5)))
    rec_delta = rec_val - 91
    rec_sign = "+" if rec_delta >= 0 else ""
    rec_arrow = "▲" if rec_delta >= 0 else "▼"
    rec_color = "#00FF99" if rec_val >= 90 else "#ffca28"
    
    # Dynamic current decisions
    al_ingot = max(0, predicted_al - 44)
    al_shots = 0
    al_wire = int(max(2, 8 + (oxygen_val - 28) * 0.2))
    saving_val = int(max(5, 18 + (224 - predicted_al) * 0.1))
    # Base64 Images
    eaf_b64 = get_base64_image("assets/eaf_furnace.jpg", "EAF")
    ladle_b64 = get_base64_image("assets/ladle_pouring.jpg", "Ladle")
    argon_b64 = get_base64_image("assets/argon_stirring.jpg", "Argon")
    ai_b64 = get_base64_image("assets/ai_engine.jpg", "AI Engine")
    lrf_b64 = get_base64_image("assets/lrf_station.jpg", "LRF")
    central_b64 = get_base64_image("assets/central_ladle.jpg", "Central Ladle")
    # SVG Definitions
    shield_svg = f"""
    <svg width="60" height="60" viewBox="0 0 100 100" style="filter: drop-shadow(0 0 8px rgba(0, 255, 153, 0.4));">
        <path d="M 50 15 Q 80 15 80 45 Q 80 75 50 90 Q 20 75 20 45 Q 20 15 50 15 Z" fill="rgba(0, 255, 153, 0.05)" stroke="#00FF99" stroke-width="3" />
        <path d="M 38 52 L 46 60 L 62 40" fill="none" stroke="#00FF99" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" />
    </svg>
    """
    
    target_svg = f"""
    <svg width="60" height="60" viewBox="0 0 100 100" style="filter: drop-shadow(0 0 8px rgba(255, 214, 0, 0.4));">
        <circle cx="50" cy="50" r="40" fill="none" stroke="#FFD54F" stroke-width="2.5" />
        <circle cx="50" cy="50" r="28" fill="none" stroke="#FF9100" stroke-width="2" />
        <circle cx="50" cy="50" r="15" fill="rgba(255, 145, 0, 0.1)" stroke="#FF3D00" stroke-width="3" />
        <line x1="82" y1="18" x2="52" y2="48" stroke="#FFD54F" stroke-width="4.5" stroke-linecap="round" />
        <polygon points="52,48 58,40 60,46" fill="#FFD54F" />
    </svg>
    """
    
    robot_logo_svg = """
    <svg width="50" height="50" viewBox="0 0 50 50" fill="none" class="dt-logo-icon">
        <circle cx="25" cy="25" r="23" stroke="#00E5FF" stroke-width="2" fill="rgba(0, 229, 255, 0.1)"/>
        <rect x="13" y="16" width="24" height="18" rx="5" stroke="#00E5FF" stroke-width="2"/>
        <circle cx="20" cy="23" r="2" fill="#00E5FF"/>
        <circle cx="30" cy="23" r="2" fill="#00E5FF"/>
        <path d="M 20 28 Q 25 31 30 28" stroke="#00E5FF" stroke-width="2" fill="none" stroke-linecap="round"/>
        <line x1="25" y1="16" x2="25" y2="11" stroke="#00E5FF" stroke-width="2"/>
        <circle cx="25" cy="10" r="1.5" fill="#00E5FF"/>
    </svg>
    """
    # Pulse SVG for health
    pulse_wave_svg = """
    <svg width="120" height="30" viewBox="0 0 120 30" style="filter: drop-shadow(0 0 4px rgba(0, 229, 255, 0.5));">
        <path d="M 0 15 L 20 15 L 25 15 L 30 5 L 35 25 L 40 15 L 45 15 L 60 15 L 65 0 L 70 30 L 75 15 L 90 15 L 95 20 L 100 10 L 105 15 L 120 15" fill="none" stroke="#00E5FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
    </svg>
    """
    # Dynamically generate checkpoints
    slag_icon = "✅" if basicity_val >= 2.8 and basicity_val <= 3.2 else "⚠️"
    temp_icon = "✅" if temperature_val >= 1600 else "❌"
    argon_icon = "✅" if oxygen_val < 45 else "⚠️"
    heat_icon = "✅" if temperature_val >= 1600 and oxygen_val < 45 else "⏳"
    
    # Recommendations
    recs_list = []
    if oxygen_val > 40:
        recs_list.append(f"<li>⚠️ High oxygen detected. Add {al_ingot} kg of Al Ingot.</li>")
    else:
        recs_list.append(f"<li>💡 Add {al_ingot} kg of Al Ingot (Optimal amount).</li>")
        
    recs_list.append("<li>💡 Do not add Al Shots (Skip recommended to avoid cost).</li>")
    
    if al_wire > 8:
        recs_list.append(f"<li>💡 Reduce Al Wire addition to {al_wire} kg (Optimize recovery).</li>")
    else:
        recs_list.append(f"<li>💡 Maintain Al Wire at {al_wire} kg.</li>")
    if basicity_val < 2.8:
        recs_list.append(f"<li>⚠️ Basicity is low ({basicity_val}). Add Lime (CaO) to slag.</li>")
    elif basicity_val > 3.2:
        recs_list.append(f"<li>⚠️ Basicity is high ({basicity_val}). Reduce synthetic slag additions.</li>")
    else:
        recs_list.append("<li>💡 Maintain Slag Basicity (V-ratio is stable at 2.8 - 3.2).</li>")
    if temperature_val < 1600:
        recs_list.append(f"<li>❌ Low temperature! Power electrodes to heat above 1600°C.</li>")
    else:
        recs_list.append("<li>💡 Temperature is optimal. Ready to send Heat to Caster.</li>")
    recs_html = "".join(recs_list)
    # Style block & HTML output
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
    st.markdown(textwrap.dedent(f"""
    <div class="dt-body">
        
        <!-- HEADER -->
        <div class="dt-header">
            <div class="dt-title-section">
                {robot_logo_svg}
                <div>
                    <h1 style="color:white; font-size:32px; font-weight:800; margin:0; line-height:1.1;">
                        DIGITAL TWIN OF LRF
                    </h1>
                    <div style="color:#00E5FF; font-size:12px; font-weight:700; letter-spacing:1px; margin-top:2px; text-transform:uppercase;">
                        — AI Powered Aluminium Optimization System —
                    </div>
                </div>
            </div>
            
            <div class="dt-header-meta">
                <div class="dt-meta-box">
                    <div class="dt-meta-label">Heat ID</div>
                    <div class="dt-meta-value">{heat_id}</div>
                </div>
                <div class="dt-meta-box">
                    <div class="dt-meta-label">Grade</div>
                    <div class="dt-meta-value blue">{grade}</div>
                </div>
                <div class="dt-meta-box" style="min-width:160px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div class="dt-meta-label" style="font-size:12px; font-weight:700; color:#ffffff;">{time_str}</div>
                            <div class="dt-meta-label" style="margin-top:1px;">{date_str}</div>
                        </div>
                        <div style="text-align:right;">
                            <span style="color:#00FF99; font-size:12px; font-weight:bold;">● Live</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- TOP METRIC CARDS -->
        <div class="dt-kpi-grid">
            
            <!-- CARD 1: TEMPERATURE -->
            <div class="dt-kpi-card temp">
                <div class="dt-kpi-header">
                    <span>🌡️ Temperature</span>
                </div>
                <div class="dt-kpi-main">
                    <div>
                        <span class="dt-kpi-value">{temperature_val}</span>
                        <span class="dt-kpi-unit">°C</span>
                        <div class="dt-kpi-change {'up' if temp_delta>=0 else 'down'}">
                            <span>{temp_arrow} {temp_sign}{temp_delta} °C</span>
                        </div>
                    </div>
                    <!-- Sparkline -->
                    <div class="dt-sparkline-container">
                        <svg viewBox="0 0 100 30" width="100%" height="100%">
                            <path d="M 0 25 L 20 20 L 40 28 L 60 15 L 80 18 L 100 5" fill="none" stroke="#FF5252" stroke-width="2" />
                        </svg>
                    </div>
                </div>
            </div>
            <!-- CARD 2: OXYGEN -->
            <div class="dt-kpi-card oxy">
                <div class="dt-kpi-header">
                    <span>🧪 Oxygen (O)</span>
                </div>
                <div class="dt-kpi-main">
                    <div>
                        <span class="dt-kpi-value">{oxygen_val}</span>
                        <span class="dt-kpi-unit">ppm</span>
                        <div class="dt-kpi-change {'green-down' if oxy_delta<=0 else 'down'}">
                            <span>{oxy_arrow} {oxy_sign}{oxy_delta} ppm</span>
                        </div>
                    </div>
                    <!-- Sparkline -->
                    <div class="dt-sparkline-container">
                        <svg viewBox="0 0 100 30" width="100%" height="100%">
                            <path d="M 0 15 L 20 22 L 40 10 L 60 18 L 80 25 L 100 28" fill="none" stroke="#00E5FF" stroke-width="2" />
                        </svg>
                    </div>
                </div>
            </div>
            <!-- CARD 3: AI PREDICTION -->
            <div class="dt-kpi-card pred">
                <div class="dt-kpi-header">
                    <span>🧠 AI Prediction</span>
                </div>
                <div class="dt-kpi-main">
                    <div>
                        <span class="dt-kpi-value">{predicted_al}</span>
                        <span class="dt-kpi-unit">kg</span>
                        <div class="dt-kpi-change {'green-down' if pred_delta<=0 else 'down'}">
                            <span>{pred_arrow} {pred_sign}{pred_delta} kg</span>
                        </div>
                    </div>
                    <!-- Sparkline -->
                    <div class="dt-sparkline-container">
                        <svg viewBox="0 0 100 30" width="100%" height="100%">
                            <path d="M 0 28 L 20 18 L 40 25 L 60 10 L 80 12 L 100 2" fill="none" stroke="#e040fb" stroke-width="2" />
                        </svg>
                    </div>
                </div>
            </div>
            <!-- CARD 4: RECOVERY -->
            <div class="dt-kpi-card rec">
                <div class="dt-kpi-header">
                    <span>♻️ Recovery</span>
                </div>
                <div class="dt-kpi-main">
                    <div>
                        <span class="dt-kpi-value">{rec_val}</span>
                        <span class="dt-kpi-unit">%</span>
                        <div class="dt-kpi-change {'up' if rec_delta>=0 else 'down'}">
                            <span>{rec_arrow} {rec_sign}{rec_delta}%</span>
                        </div>
                    </div>
                    <!-- Sparkline -->
                    <div class="dt-sparkline-container">
                        <svg viewBox="0 0 100 30" width="100%" height="100%">
                            <path d="M 0 20 L 20 22 L 40 18 L 60 15 L 80 10 L 100 5" fill="none" stroke="#00FF99" stroke-width="2" />
                        </svg>
                    </div>
                </div>
            </div>
        </div>
        <!-- PROCESS FLOW PIPELINE -->
        <div class="dt-flow-section">
            <div class="dt-flow-title">LIVE PROCESS FLOW</div>
            
            <div class="dt-flow-grid">
                <div class="dt-flow-item eaf">
                    <div class="dt-flow-label">🔥 EAF</div>
                    <div class="dt-flow-img-wrapper">
                        <img class="dt-flow-img" src="{eaf_b64}" alt="EAF" />
                    </div>
                </div>
                <div class="dt-flow-arrow">➔</div>
                
                <div class="dt-flow-item ladle">
                    <div class="dt-flow-label">🍯 LADLE</div>
                    <div class="dt-flow-img-wrapper">
                        <img class="dt-flow-img" src="{ladle_b64}" alt="Ladle" />
                    </div>
                </div>
                
                <div class="dt-flow-arrow">➔</div>
                
                <div class="dt-flow-item argon">
                    <div class="dt-flow-label">🌀 ARGON STIRRING</div>
                    <div class="dt-flow-img-wrapper">
                        <img class="dt-flow-img" src="{argon_b64}" alt="Argon" />
                    </div>
                </div>
                
                <div class="dt-flow-arrow">➔</div>
                
                <div class="dt-flow-item ai">
                    <div class="dt-flow-label">🤖 AI ENGINE</div>
                    <div class="dt-flow-img-wrapper">
                        <img class="dt-flow-img" src="{ai_b64}" alt="AI Engine" />
                    </div>
                </div>
                
                <div class="dt-flow-arrow">➔</div>
                
                <div class="dt-flow-item lrf">
                    <div class="dt-flow-label">🏭 LRF</div>
                    <div class="dt-flow-img-wrapper">
                        <img class="dt-flow-img" src="{lrf_b64}" alt="LRF" />
                    </div>
                </div>
            </div>
            
            <!-- Nodes Connection Track -->
            <div class="dt-flow-track">
                <div class="dt-flow-line"></div>
                <div class="dt-flow-node eaf"></div>
                <div class="dt-flow-node ladle"></div>
                <div class="dt-flow-node argon"></div>
                <div class="dt-flow-node ai"></div>
                <div class="dt-flow-node lrf"></div>
            </div>
        </div>
        <!-- TRIPLE COLUMNS LAYOUT -->
        <div class="dt-bottom-row">
            
            <!-- COL 1: CURRENT AI DECISION -->
            <div class="dt-panel">
                <div class="dt-panel-title">CURRENT AI DECISION</div>
                
                <div class="dt-decision-item">
                    <div class="dt-decision-left">
                        <span>⬜</span>
                        <span>Al Ingot</span>
                    </div>
                    <div class="dt-decision-right">
                        <span class="dt-decision-val" style="color:#00FF99;">{al_ingot} kg</span>
                        <span class="dt-badge optimal">OPTIMAL</span>
                    </div>
                </div>
                
                <div class="dt-decision-item">
                    <div class="dt-decision-left">
                        <span>⚫</span>
                        <span>Al Shots</span>
                    </div>
                    <div class="dt-decision-right">
                        <span class="dt-decision-val" style="color:#8fa7c7;">{al_shots} kg</span>
                        <span class="dt-badge skip" style="border:1px solid #555; color:#888;">SKIP</span>
                    </div>
                </div>
                
                <div class="dt-decision-item">
                    <div class="dt-decision-left">
                        <span>🌀</span>
                        <span>Al Wire</span>
                    </div>
                    <div class="dt-decision-right">
                        <span class="dt-decision-val" style="color:#00E5FF;">{al_wire} kg</span>
                        <span class="dt-badge reduced">REDUCED</span>
                    </div>
                </div>
                
                <div class="dt-decision-item">
                    <div class="dt-decision-left">
                        <span>💾</span>
                        <span>Predicted Aluminium Addition</span>
                    </div>
                    <div class="dt-decision-right">
                        <span class="dt-decision-val" style="color:#e040fb;">{predicted_al} kg</span>
                        <span class="dt-badge predicted">AI PREDICTED</span>
                    </div>
                </div>
                
                <div class="dt-decision-item">
                    <div class="dt-decision-left">
                        <span>🔄</span>
                        <span>Expected Recovery</span>
                    </div>
                    <div class="dt-decision-right">
                        <span class="dt-decision-val" style="color:#00FF99;">{rec_val}%</span>
                        <span class="dt-badge excellent">EXCELLENT</span>
                    </div>
                </div>
                
                <div class="dt-decision-item">
                    <div class="dt-decision-left">
                        <span>💰</span>
                        <span>Estimated Saving vs Plant Avg.</span>
                    </div>
                    <div class="dt-decision-right">
                        <span class="dt-decision-val" style="color:#00FF99;">{saving_val} kg</span>
                        <span class="dt-badge saving">COST SAVING</span>
                    </div>
                </div>
            </div>
            <!-- COL 2: HOLOGRAM CENTER -->
            <div class="dt-panel">
                <div class="dt-panel-title" style="text-align:center;">LADLE DYNAMICS</div>
                <div class="dt-holo-container">
                    <div class="dt-holo-ring"></div>
                    <div class="dt-holo-img-wrapper">
                        <img class="dt-holo-img" src="{central_b64}" alt="Molten Ladle" />
                    </div>
                </div>
            </div>
            <!-- COL 3: STATUS & AI RECOMMENDATION -->
            <div class="dt-panel">
                <div class="dt-panel-title">PROCESS STATUS &amp; ACTIONS</div>
                
                <!-- Process Status Subpanel -->
                <div class="dt-subpanel-title">Process Status</div>
                <div class="dt-status-container">
                    <div class="dt-status-list">
                        <div class="dt-status-item">
                            <span>{slag_icon}</span>
                            <span>Slag Condition: <b>Reducing</b></span>
                        </div>
                        <div class="dt-status-item">
                            <span>{temp_icon}</span>
                            <span>Temperature: <b>{"Stable" if temperature_val>=1600 else "Low"}</b></span>
                        </div>
                        <div class="dt-status-item">
                            <span>{argon_icon}</span>
                            <span>Argon Stirring: <b>{"Normal" if oxygen_val<45 else "High O2"}</b></span>
                        </div>
                        <div class="dt-status-item">
                            <span>{heat_icon}</span>
                            <span>Heat Condition: <b>{"Ready" if (temperature_val>=1600 and oxygen_val<45) else "Critical"}</b></span>
                        </div>
                    </div>
                    <div>
                        {shield_svg}
                    </div>
                </div>
                
                <!-- AI Recommendations Subpanel -->
                <div class="dt-subpanel-title">AI Recommendations</div>
                <div class="dt-recs-container">
                    <ul class="dt-recs-list" style="list-style:none; padding-left:0; margin:0;">
                        {recs_html}
                    </ul>
                    <div>
                        {target_svg}
                    </div>
                </div>
            </div>
        </div>
        <!-- DIGITAL TWIN HEALTH PROGRESS BAR -->
        <div class="dt-health-section">
            <div class="dt-health-title-wrapper">
                {pulse_wave_svg}
                <span class="dt-health-title">DIGITAL TWIN HEALTH</span>
            </div>
            
            <div class="dt-health-bar-container">
                <div class="dt-health-bar-fill" style="width: {health_val}%;"></div>
            </div>
            
            <div class="dt-health-text">{health_val}%</div>
        </div>
        <!-- BOTTOM CHEMISTRY COMPOSITION CARDS -->
        <div class="dt-chem-grid">
            
            <div class="dt-chem-card basicity">
                <div class="dt-chem-icon-box">⚗️</div>
                <div class="dt-chem-info">
                    <span class="dt-chem-label">Slag Basicity</span>
                    <span class="dt-chem-val">{basicity_val}</span>
                </div>
            </div>
            
            <div class="dt-chem-card feo">
                <div class="dt-chem-icon-box">🛡️</div>
                <div class="dt-chem-info">
                    <span class="dt-chem-label">FeO in Slag</span>
                    <span class="dt-chem-val">{feo_val}%</span>
                </div>
            </div>
            
            <div class="dt-chem-card c">
                <div class="dt-chem-icon-box">C</div>
                <div class="dt-chem-info">
                    <span class="dt-chem-label">C in Steel</span>
                    <span class="dt-chem-val">{c_val}%</span>
                </div>
            </div>
            
            <div class="dt-chem-card mn">
                <div class="dt-chem-icon-box">Mn</div>
                <div class="dt-chem-info">
                    <span class="dt-chem-label">Mn in Steel</span>
                    <span class="dt-chem-val">{mn_val}%</span>
                </div>
            </div>
            
            <div class="dt-chem-card si">
                <div class="dt-chem-icon-box">Si</div>
                <div class="dt-chem-info">
                    <span class="dt-chem-label">Si in Steel</span>
                    <span class="dt-chem-val">{si_val}%</span>
                </div>
            </div>
            
            <div class="dt-chem-card n">
                <div class="dt-chem-icon-box">N</div>
                <div class="dt-chem-info">
                    <span class="dt-chem-label">N in Steel</span>
                    <span class="dt-chem-val">{n_val} ppm</span>
                </div>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)
# ============================================================
# MAIN APPLICATION ROUTING
# ============================================================
def main():
    st.sidebar.markdown(textwrap.dedent("""
    <div style="text-align:center; padding:10px 0;">
        <h2 style="color:#00E5FF; margin-bottom:0; font-weight:800; text-shadow:0 0 10px rgba(0,229,255,0.4);">
        ⚡ LRF CONTROL
        </h2>
        <span style="color:#8fa7c7; font-size:11px; font-weight:600; letter-spacing:1.5px; text-transform:uppercase;">
            Optimization Unit
        </span>
    </div>
    """), unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    # Navigation Selector
    page = st.sidebar.selectbox("Navigate Dashboard", ["Digital Twin of LRF", "Management Dashboard"])
    
    if page == "Management Dashboard":
        st.sidebar.markdown("### Config Summary")
        st.sidebar.info(
            "Executive view for monitoring aluminum consumption, AI model performance metrics, and estimated plant savings."
        )
        management_dashboard()
    else:
        st.sidebar.markdown("### Twin Parameters")
        
        # Interactive Controls
        heat_id = st.sidebar.text_input("Heat ID", value="HEAT_2026_06129")
        grade = st.sidebar.text_input("Grade", value="FE550DLMH")
        
        st.sidebar.markdown("#### Real-time Sensors")
        temperature_val = st.sidebar.slider("Temperature (°C)", min_value=1500, max_value=1700, value=1612, step=1)
        oxygen_val = st.sidebar.slider("Oxygen Content (ppm)", min_value=5, max_value=100, value=28, step=1)
        
        st.sidebar.markdown("#### Chemistry")
        basicity_val = st.sidebar.slider("Slag Basicity (V-ratio)", min_value=1.0, max_value=4.0, value=2.92, step=0.01)
        feo_val = st.sidebar.slider("FeO in Slag (%)", min_value=1.0, max_value=30.0, value=8.6, step=0.1)
        c_val = st.sidebar.slider("C in Steel (%)", min_value=0.01, max_value=1.00, value=0.08, step=0.01)
        mn_val = st.sidebar.slider("Mn in Steel (%)", min_value=0.05, max_value=1.50, value=0.42, step=0.01)
        si_val = st.sidebar.slider("Si in Steel (%)", min_value=0.05, max_value=1.00, value=0.28, step=0.01)
        n_val = st.sidebar.slider("N in Steel (ppm)", min_value=10, max_value=150, value=48, step=1)
        
        st.sidebar.markdown("#### System Settings")
        health_val = st.sidebar.slider("Digital Twin Health (%)", min_value=0, max_value=100, value=82, step=1)
        
        digital_twin_dashboard(
            heat_id=heat_id,
            grade=grade,
            temperature_val=temperature_val,
            oxygen_val=oxygen_val,
            basicity_val=basicity_val,
            feo_val=feo_val,
            c_val=c_val,
            mn_val=mn_val,
            si_val=si_val,
            n_val=n_val,
            health_val=health_val
        )
if __name__ == "__main__":
    main()