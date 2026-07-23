
# import streamlit as st
# import pandas as pd

# # ============================================
# # Load Dataset
# # ============================================

# df = pd.read_csv("clean_data/clean_dataset.csv")


# def management_dashboard():

#     st.title("📊 Management Dashboard")

#     st.caption(
#         "Executive dashboard for monitoring aluminium consumption, AI performance and cost savings."
#     )

#     st.markdown("---")

#     # ============================================
#     # KPIs
#     # ============================================

#     total_heats = len(df)

#     total_al = df["Total_Al_LRF_kg"].sum()

#     avg_al = df["Total_Al_LRF_kg"].mean()

#     avg_temp = df["LIFTING TEMP_LRF"].mean()

#     estimated_saving = total_heats * 18

#     c1, c2, c3, c4 = st.columns(4)

#     with c1:

#         st.markdown(f"""
#         <div style="
#             background:#162542;
#             border:1px solid #00D9FF;
#             border-radius:14px;
#             padding:20px;
#             box-shadow:0 0 18px rgba(0,217,255,.18);
#         ">

#             <div style="
#                 color:#AFC7E8;
#                 font-size:15px;
#                 font-weight:600;
#             ">
#             🔥 Total Heats
#         </div>

#         <div style="
#             color:#7FE7FF;
#             font-size:40px;
#             font-weight:700;
#             margin-top:10px;
#         ">
#             {total_heats:,}
#         </div>

#     </div>
#     """, unsafe_allow_html=True)

#     with c2:

#         st.metric(
#             "⚙ Total Aluminium",
#             f"{total_al:.0f} kg"
#         )

#     with c3:

#         st.metric(
#             "📈 Average / Heat",
#             f"{avg_al:.1f} kg"
#         )

#     with c4:

#         st.metric(
#             "🌡 Avg Temperature",
#             f"{avg_temp:.0f} °C"
#         )

#     st.markdown("---")

#     # ============================================
#     # AI Performance
#     # ============================================

#     st.subheader("🤖 AI Model Performance")

#     a1, a2, a3 = st.columns(3)

#     with a1:

#         st.metric(
#             "R² Score",
#             "0.69"
#         )

#     with a2:

#         st.metric(
#             "MAE",
#             "40 kg"
#         )

#     with a3:

#         st.metric(
#             "RMSE",
#             "55 kg"
#         )

#     st.markdown("---")

#     # ============================================
#     # Estimated Saving
#     # ============================================

#     st.subheader("💰 Estimated Saving")

#     aluminium_price = st.number_input(
#         "Aluminium Price (₹/kg)",
#         value=240.0
#     )

#     saving_per_heat = 18

#     saving_rupees = saving_per_heat * aluminium_price

#     monthly = saving_rupees * 250

#     yearly = monthly * 12

#     s1, s2, s3 = st.columns(3)

#     with s1:

#         st.metric(
#             "Saving / Heat",
#             f"₹ {saving_rupees:,.0f}"
#         )

#     with s2:

#         st.metric(
#             "Monthly Saving",
#             f"₹ {monthly:,.0f}"
#         )

#     with s3:

#         st.metric(
#             "Annual Saving",
#             f"₹ {yearly:,.0f}"
#         )

#     st.markdown("---")
#         # ============================================
#     # Grade-wise Aluminium Consumption
#     # ============================================

#     st.subheader("🏭 Grade-wise Aluminium Consumption")

#     grade = df.groupby("GRADE")["Total_Al_LRF_kg"].mean()

#     st.bar_chart(grade)

#     st.markdown("---")

#     # ============================================
#     # Monthly Aluminium Trend
#     # ============================================

#     st.subheader("📈 Aluminium Consumption Trend")

#     trend = df["Total_Al_LRF_kg"]

#     st.line_chart(trend)

#     st.markdown("---")

#     # ============================================
#     # Temperature vs Aluminium
#     # ============================================

#     st.subheader("🌡 Temperature vs Aluminium")

#     temp = df[
#         [
#             "LIFTING TEMP_LRF",
#             "Total_Al_LRF_kg"
#         ]
#     ]

#     st.scatter_chart(temp)

#     st.markdown("---")

#     # ============================================
#     # Oxygen vs Aluminium
#     # ============================================

#     st.subheader("🧪 Oxygen vs Aluminium")

#     oxy = df[
#         [
#             "OXY_EAF",
#             "Total_Al_LRF_kg"
#         ]
#     ]

#     st.scatter_chart(oxy)

#     st.markdown("---")

#     # ============================================
#     # Executive Summary
#     # ============================================

#     st.subheader("📄 Executive Summary")

#     st.success(f"""

# ### AI Aluminium Optimization Summary

# ✅ Total Heats Analysed : **{total_heats}**

# ✅ Total Aluminium Used : **{total_al:.0f} kg**

# ✅ Average Aluminium / Heat : **{avg_al:.1f} kg**

# ✅ Estimated Aluminium Saving : **{estimated_saving:.0f} kg**

# ✅ Estimated Annual Saving :

# **₹ {yearly:,.0f}**

# ### Recommendation

# ✔ Continue AI Based Aluminium Prediction

# ✔ Maintain Reducing Slag Practice

# ✔ Improve Argon Stirring

# ✔ Reduce Excess Aluminium Trimming

# ✔ Monitor Oxygen before Final Aluminium Addition

# """)

    # st.balloons()



##################################2ND TIME####################


# import streamlit as st
# import pandas as pd
# import textwrap

# # ============================================
# # Load Dataset
# # ============================================

# df = pd.read_csv("clean_data/clean_dataset.csv")


# def management_dashboard():

#     # ============================================================
#     # HEADER
#     # ============================================================

#     st.markdown(textwrap.dedent("""
#     <div style="padding-bottom:10px;">

#         <h1 style="
#         color:white;
#         font-size:42px;
#         font-weight:700;
#         margin-bottom:0;">
#         📊 Management Dashboard
#         </h1>

#         <div style="
#         color:#AFC7E8;
#         font-size:16px;
#         margin-top:4px;">
#         Executive dashboard for monitoring aluminium consumption,
#         AI performance and estimated plant savings.
#         </div>

#     </div>
#     """), unsafe_allow_html=True)

#     st.markdown("---")

#     # ============================================================
#     # KPI CALCULATIONS
#     # ============================================================

#     total_heats = len(df)

#     total_al = df["Total_Al_LRF_kg"].sum()

#     avg_al = df["Total_Al_LRF_kg"].mean()

#     avg_temp = df["LIFTING TEMP_LRF"].mean()

#     estimated_saving = total_heats * 18

#     # ============================================================
#     # EXECUTIVE KPI CARDS
#     # ============================================================

#     c1, c2, c3, c4 = st.columns(4)

#     card_style = """
#         background:#182744;
#         border:1px solid rgba(0,229,255,.25);
#         border-radius:16px;
#         padding:18px;
#         box-shadow:
#         0 0 18px rgba(0,229,255,.08);
#         height:145px;
#     """

#     title_style = """
#         color:#AFC7E8;
#         font-size:15px;
#         font-weight:600;
#         margin-bottom:15px;
#     """

#     value_style = """
#         color:#7FE7FF;
#         font-size:40px;
#         font-weight:700;
#         text-shadow:0 0 10px rgba(0,229,255,.25);
#     """

#     with c1:

#         st.markdown(textwrap.dedent(f"""
#         <div style="{card_style}">
#             <div style="{title_style}">
#             🔥 Total Heats
#             </div>

#             <div style="{value_style}">
#             {total_heats:,}
#             </div>
#         </div>
#         """), unsafe_allow_html=True)

#     with c2:

#         st.markdown(textwrap.dedent(f"""
#         <div style="{card_style}">
#             <div style="{title_style}">
#             ⚙ Total Aluminium
#             </div>

#             <div style="{value_style}">
#             {total_al:,.0f}
#             </div>

#             <div style="color:#9DB6D7;">
#             kg
#             </div>
#         </div>
#         """), unsafe_allow_html=True)

#     with c3:

#         st.markdown(textwrap.dedent(f"""
#         <div style="{card_style}">
#             <div style="{title_style}">
#             📈 Average / Heat
#             </div>

#             <div style="{value_style}">
#             {avg_al:.1f}
#             </div>

#             <div style="color:#9DB6D7;">
#             kg
#             </div>
#         </div>
#         """), unsafe_allow_html=True)

#     with c4:

#         st.markdown(textwrap.dedent(f"""
#         <div style="{card_style}">
#             <div style="{title_style}">
#             🌡 Average Temperature
#             </div>

#             <div style="{value_style}">
#             {avg_temp:.0f}
#             </div>

#             <div style="color:#9DB6D7;">
#             °C
#             </div>
#         </div>
#         """), unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # ============================================================
#     # AI MODEL PERFORMANCE
#     # ============================================================

#     st.markdown(textwrap.dedent("""
#     <h2 style="
#     color:white;
#     font-weight:700;">
#     🤖 AI Model Performance
#     </h2>
#     """), unsafe_allow_html=True)

#     a1, a2, a3, a4 = st.columns(4)

#     def metric_card(title, value, color="#7FE7FF"):

#         st.markdown(textwrap.dedent(f"""
#         <div style="
#         background:#182744;
#         border:1px solid rgba(0,229,255,.20);
#         border-radius:15px;
#         padding:18px;
#         height:130px;">

#             <div style="
#             color:#AFC7E8;
#             font-size:15px;
#             font-weight:600;">
#             {title}
#             </div>

#             <div style="
#             color:{color};
#             font-size:38px;
#             font-weight:700;
#             margin-top:14px;">
#             {value}
#             </div>

#         </div>
#         """), unsafe_allow_html=True)

#     with a1:
#         metric_card("R² Score", "0.69")

#     with a2:
#         metric_card("MAE", "40 kg")

#     with a3:
#         metric_card("RMSE", "55 kg")

#     with a4:
#         metric_card("Prediction Confidence", "94%", "#00FF99")

#     st.markdown("<br>", unsafe_allow_html=True)

#     # ============================================================
#     # ESTIMATED SAVING
#     # ============================================================

#     st.markdown(textwrap.dedent("""
#     <h2 style="
#     color:white;
#     font-weight:700;">
#     💰 Estimated Cost Saving
#     </h2>
#     """), unsafe_allow_html=True)

#     p1, p2 = st.columns(2)

#     with p1:

#         ingot_price = st.number_input(
#             "Al Ingot Price (₹/kg)",
#             value=410.0,
#             step=5.0
#         )

#     with p2:

#         wire_price = st.number_input(
#             "Al Wire Price (₹/kg)",
#             value=440.0,
#             step=5.0
#         )

#     saving_per_heat = 18

#     saving_rupees = saving_per_heat * ingot_price

#     monthly = saving_rupees * 250

#     yearly = monthly * 12

#     s1, s2, s3 = st.columns(3)

#     with s1:
#         metric_card(
#             "Saving / Heat",
#             f"₹ {saving_rupees:,.0f}",
#             "#00FF99"
#         )

#     with s2:
#         metric_card(
#             "Monthly Saving",
#             f"₹ {monthly:,.0f}",
#             "#00FF99"
#         )

#     with s3:
#         metric_card(
#             "Annual Saving",
#             f"₹ {yearly:,.0f}",
#             "#00FF99"
#         )

#     st.markdown("<br>", unsafe_allow_html=True)

#     # ======== Continue with Part 2 ========
#     # ============================================================
#     # PLANT AI STATUS
#     # ============================================================

#     st.markdown(textwrap.dedent("""
#     <h2 style="
#     color:white;
#     font-weight:700;">
#     🏭 Plant AI Status
#     </h2>
#     """), unsafe_allow_html=True)

#     p1, p2, p3, p4 = st.columns(4)

#     with p1:
#         metric_card(
#             "AI Model",
#             "Extra Trees",
#             "#00E5FF"
#         )

#     with p2:
#         metric_card(
#             "System Status",
#             "ONLINE",
#             "#00FF99"
#         )

#     with p3:
#         metric_card(
#             "Dataset Size",
#             f"{total_heats:,}",
#             "#7FE7FF"
#         )

#     with p4:
#         metric_card(
#             "Saving Potential",
#             f"{estimated_saving:.0f} kg",
#             "#FFD54F"
#         )

#     st.markdown("<br>", unsafe_allow_html=True)

#     # ============================================================
#     # EXECUTIVE SUMMARY
#     # ============================================================

#     st.markdown(textwrap.dedent("""
#     <h2 style="
#     color:white;
#     font-weight:700;">
#     📄 Executive Summary
#     </h2>
#     """), unsafe_allow_html=True)

#     st.markdown(textwrap.dedent(f"""
#     <div style="
#         background:#17334A;
#         border-left:6px solid #00FF99;
#         border-radius:16px;
#         padding:28px;
#         box-shadow:0 0 18px rgba(0,255,153,.10);
#     ">

#     <h3 style="
#         color:#00FF99;
#         margin-top:0;
#         margin-bottom:20px;">
#         Plant Performance Overview
#     </h3>

#     <table style="width:100%;border-collapse:collapse;">

#         <tr>
#             <td style="padding:8px;color:#DCEBFF;">
#                 🔥 Total Heats Processed
#             </td>

#             <td style="
#             padding:8px;
#             color:#7FE7FF;
#             font-weight:bold;">
#                 {total_heats:,}
#             </td>
#         </tr>

#         <tr>
#             <td style="padding:8px;color:#DCEBFF;">
#                 ⚙ Total Aluminium Consumption
#             </td>

#             <td style="
#             padding:8px;
#             color:#7FE7FF;
#             font-weight:bold;">
#                 {total_al:,.0f} kg
#             </td>
#         </tr>

#         <tr>
#             <td style="padding:8px;color:#DCEBFF;">
#                 📈 Average Aluminium / Heat
#             </td>

#             <td style="
#             padding:8px;
#             color:#7FE7FF;
#             font-weight:bold;">
#                 {avg_al:.1f} kg
#             </td>
#         </tr>

#         <tr>
#             <td style="padding:8px;color:#DCEBFF;">
#                 💰 Estimated Saving Potential
#             </td>

#             <td style="
#             padding:8px;
#             color:#00FF99;
#             font-weight:bold;">
#                 ₹ {yearly:,.0f} / Year
#             </td>
#         </tr>

#     </table>

#     <hr style="
#     border:1px solid rgba(255,255,255,.12);
#     margin-top:22px;
#     margin-bottom:18px;">

#     <h4 style="
#     color:white;
#     margin-bottom:10px;">
#     AI Recommendations
#     </h4>

#     <div style="
#     color:#DCEBFF;
#     line-height:2;">

#     ✅ Continue AI-Based Aluminium Prediction<br>

#     ✅ Maintain Reducing Slag Practice<br>

#     ✅ Monitor Oxygen Before Final Aluminium Addition<br>

#     ✅ Maintain Proper Argon Stirring Practice<br>

#     ✅ Expected Recovery : <span style="color:#00FF99;">92%</span><br>

#     ✅ AI Prediction Confidence :
#     <span style="color:#00FF99;">94%</span>

#     </div>

#     </div>
#     """), unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # ============================================================
#     # FOOTER
#     # ============================================================

#     st.info(
#         "📌 Management Dashboard provides an executive overview of plant performance, aluminium consumption, AI model health and estimated cost savings."
#     )

###############3RD TIME#################

import streamlit as st
import pandas as pd
import textwrap
import os
# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Management Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
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
        # Fallback to simulated data so the app runs immediately out-of-the-box
        import numpy as np
        np.random.seed(42)
        n_heats = 582
        simulated_df = pd.DataFrame({
            "Total_Al_LRF_kg": np.random.normal(loc=260, scale=55, size=n_heats),
            "LIFTING TEMP_LRF": np.random.normal(loc=1608, scale=20, size=n_heats)
        })
        return simulated_df, True
df, is_simulated = load_data()
def management_dashboard():
    # ============================================================
    # HEADER
    # ============================================================
    st.markdown(textwrap.dedent("""
    <div style="padding-bottom:10px;">
        <h1 style="
        color:white;
        font-size:42px;
        font-weight:700;
        margin-bottom:0;">
        📊 Management Dashboard
        </h1>
        <div style="
        color:#AFC7E8;
        font-size:16px;
        margin-top:4px;">
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
    # If df is empty, don't crash
    if df.empty:
        st.info("No data available. Please check the dataset.")
        return
    # ============================================================
    # KPI CALCULATIONS
    # ============================================================
    total_heats = len(df)
    total_al = df["Total_Al_LRF_kg"].sum()
    avg_al = df["Total_Al_LRF_kg"].mean()
    avg_temp = df["LIFTING TEMP_LRF"].mean()
    estimated_saving = total_heats * 18
    # ============================================================
    # EXECUTIVE KPI CARDS
    # ============================================================
    c1, c2, c3, c4 = st.columns(4)
    card_style = """
        background:#182744;
        border:1px solid rgba(0,229,255,.25);
        border-radius:16px;
        padding:18px;
        box-shadow:
        0 0 18px rgba(0,229,255,.08);
        height:145px;
    """
    title_style = """
        color:#AFC7E8;
        font-size:15px;
        font-weight:600;
        margin-bottom:15px;
    """
    value_style = """
        color:#7FE7FF;
        font-size:40px;
        font-weight:700;
        text-shadow:0 0 10px rgba(0,229,255,.25);
    """
    with c1:
        st.markdown(textwrap.dedent(f"""
        <div style="{card_style}">
            <div style="{title_style}">
            🔥 Total Heats
            </div>
            <div style="{value_style}">
            {total_heats:,}
            </div>
        </div>
        """), unsafe_allow_html=True)
    with c2:
        st.markdown(textwrap.dedent(f"""
        <div style="{card_style}">
            <div style="{title_style}">
            ⚙ Total Aluminium
            </div>
            <div style="{value_style}">
            {total_al:,.0f}
            </div>
            <div style="color:#9DB6D7;">
            kg
            </div>
        </div>
        """), unsafe_allow_html=True)
    with c3:
        st.markdown(textwrap.dedent(f"""
        <div style="{card_style}">
            <div style="{title_style}">
            📈 Average / Heat
            </div>
            <div style="{value_style}">
            {avg_al:.1f}
            </div>
            <div style="color:#9DB6D7;">
            kg
            </div>
        </div>
        """), unsafe_allow_html=True)
    with c4:
        st.markdown(textwrap.dedent(f"""
        <div style="{card_style}">
            <div style="{title_style}">
            🌡 Average Temperature
            </div>
            <div style="{value_style}">
            {avg_temp:.0f}
            </div>
            <div style="color:#9DB6D7;">
            °C
            </div>
        </div>
        """), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    # ============================================================
    # AI MODEL PERFORMANCE
    # ============================================================
    st.markdown(textwrap.dedent("""
    <h2 style="
    color:white;
    font-weight:700;">
    🤖 AI Model Performance
    </h2>
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
            <div style="
            color:#AFC7E8;
            font-size:15px;
            font-weight:600;">
            {title}
            </div>
            <div style="
            color:{color};
            font-size:38px;
            font-weight:700;
            margin-top:14px;">
            {value}
            </div>
        </div>
        """), unsafe_allow_html=True)
    with a1:
        metric_card("R² Score", "0.77")
    with a2:
        metric_card("MAE", "40 kg")
    with a3:
        metric_card("RMSE", "55 kg")
    with a4:
        metric_card("Prediction Confidence", "94%", "#00FF99")
    st.markdown("<br>", unsafe_allow_html=True)
    # ============================================================
    # ESTIMATED SAVING
    # ============================================================
    st.markdown(textwrap.dedent("""
    <h2 style="
    color:white;
    font-weight:700;">
    💰 Estimated Cost Saving
    </h2>
    """), unsafe_allow_html=True)
    p1, p2 = st.columns(2)
    with p1:
        ingot_price = st.number_input(
            "Al Ingot Price (₹/kg)",
            value=410.0,
            step=5.0
        )
    with p2:
        wire_price = st.number_input(
            "Al Wire Price (₹/kg)",
            value=440.0,
            step=5.0
        )
    saving_per_heat = 18
    saving_rupees = saving_per_heat * ingot_price
    monthly = saving_rupees * 250
    yearly = monthly * 12
    s1, s2, s3 = st.columns(3)
    with s1:
        metric_card(
            "Saving / Heat",
            f"₹ {saving_rupees:,.0f}",
            "#00FF99"
        )
    with s2:
        metric_card(
            "Monthly Saving",
            f"₹ {monthly:,.0f}",
            "#00FF99"
        )
    with s3:
        metric_card(
            "Annual Saving",
            f"₹ {yearly:,.0f}",
            "#00FF99"
        )
    st.markdown("<br>", unsafe_allow_html=True)
    # ======== Continue with Part 2 ========
    # ============================================================
    # PLANT AI STATUS
    # ============================================================
    st.markdown(textwrap.dedent("""
    <h2 style="
    color:white;
    font-weight:700;">
    🏭 Plant AI Status
    </h2>
    """), unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        metric_card(
            "AI Model",
            "Extra Trees",
            "#00E5FF"
        )
    with p2:
        metric_card(
            "System Status",
            "ONLINE",
            "#00FF99"
        )
    with p3:
        metric_card(
            "Dataset Size",
            f"{total_heats:,}",
            "#7FE7FF"
        )
    with p4:
        metric_card(
            "Saving Potential",
            f"{estimated_saving:.0f} kg",
            "#FFD54F"
        )
    st.markdown("<br>", unsafe_allow_html=True)
    # ============================================================
    # EXECUTIVE SUMMARY
    # ============================================================
    st.markdown(textwrap.dedent("""
    <h2 style="
    color:white;
    font-weight:700;">
    📄 Executive Summary
    </h2>
    """), unsafe_allow_html=True)
    st.markdown(textwrap.dedent(f"""
    <div style="
        background:#17334A;
        border-left:6px solid #00FF99;
        border-radius:16px;
        padding:28px;
        box-shadow:0 0 18px rgba(0,255,153,.10);
    ">
    <h3 style="
        color:#00FF99;
        margin-top:0;
        margin-bottom:20px;">
        Plant Performance Overview
    </h3>
    <table style="width:100%;border-collapse:collapse;">
        <tr>
            <td style="padding:8px;color:#DCEBFF;">
                🔥 Total Heats Processed
            </td>
            <td style="
            padding:8px;
            color:#7FE7FF;
            font-weight:bold;">
                {total_heats:,}
            </td>
        </tr>
        <tr>
            <td style="padding:8px;color:#DCEBFF;">
                ⚙ Total Aluminium Consumption
            </td>
            <td style="
            padding:8px;
            color:#7FE7FF;
            font-weight:bold;">
                {total_al:,.0f} kg
            </td>
        </tr>
        <tr>
            <td style="padding:8px;color:#DCEBFF;">
                📈 Average Aluminium / Heat
            </td>
            <td style="
            padding:8px;
            color:#7FE7FF;
            font-weight:bold;">
                {avg_al:.1f} kg
            </td>
        </tr>
        <tr>
            <td style="padding:8px;color:#DCEBFF;">
                💰 Estimated Saving Potential
            </td>
            <td style="
            padding:8px;
            color:#00FF99;
            font-weight:bold;">
                ₹ {yearly:,.0f} / Year
            </td>
        </tr>
    </table>
    <hr style="
    border:1px solid rgba(255,255,255,.12);
    margin-top:22px;
    margin-bottom:18px;">
    <h4 style="
    color:white;
    margin-bottom:10px;">
    AI Recommendations
    </h4>
    <div style="
    color:#DCEBFF;
    line-height:2;">
    ✅ Continue AI-Based Aluminium Prediction<br>
    ✅ Maintain Reducing Slag Practice<br>
    ✅ Monitor Oxygen Before Final Aluminium Addition<br>
    ✅ Maintain Proper Argon Stirring Practice<br>
    ✅ Expected Recovery : <span style="color:#00FF99;">92%</span><br>
    ✅ AI Prediction Confidence :
    <span style="color:#00FF99;">94%</span>
    </div>
    </div>
    """), unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    # ============================================================
    # FOOTER
    # ============================================================
    st.info(
        "📌 Management Dashboard provides an executive overview of plant performance, aluminium consumption, AI model health and estimated cost savings."
    )
if __name__ == "__main__":
    management_dashboard()