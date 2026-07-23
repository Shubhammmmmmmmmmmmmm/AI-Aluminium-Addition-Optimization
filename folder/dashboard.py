
############ 2ND TIME #############
import streamlit as st
import pandas as pd

# ==========================================================
# COMPONENTS
# ==========================================================

from folder.components.header import header
from folder.components.kpi_cards import show_kpis
from folder.components.gauges import aluminium_gauge
from folder.components.live_trends import live_trends
from folder.components.alerts_panel import alerts_panel
from folder.components.heat_selector import heat_selector

# ==========================================================
# AI
# ==========================================================

from utils.prediction import predict_heat
from utils.recommendation import generate_recommendation

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_dataset():
    return pd.read_csv("clean_data/clean_dataset.csv")


df = load_dataset()

# ==========================================================
# DASHBOARD
# ==========================================================
def dashboard():

  

    # ======================================================
    # DATA SOURCE
    # ======================================================

    if (
        st.session_state.get("prediction_done", False)
        and "dashboard_data" in st.session_state
    ):

        dashboard_data = st.session_state["dashboard_data"]

        selected_heat = pd.Series(
            dashboard_data["selected_heat"]
        )

        recommendation = dashboard_data["recommendation"]

        predicted_al = recommendation["Predicted_Al"]

    else:

        selected_heat = heat_selector(df)

  

        prediction = predict_heat(selected_heat)

        recommendation = generate_recommendation(prediction)

        predicted_al = recommendation["Predicted_Al"]

    oxygen = st.session_state.get("oxygen", 450.0)

    # ======================================================
    # HEADER
    # ======================================================

    header(selected_heat)

    st.markdown("---")

    # ------------------------------------------------------
    # KPI Cards
    # ------------------------------------------------------

    show_kpis(
        selected_heat,
        recommendation
    )
 
    st.markdown("---")

    # ======================================================
    # MAIN LAYOUT
    # ======================================================

    left, right = st.columns([2.8, 1])

    # ======================================================
    # LEFT PANEL
    # ======================================================

    with left:

        aluminium_gauge(
            value=predicted_al,
            confidence=recommendation["Confidence"]
        )

        st.write("")

        live_trends(
            selected_heat,
            recommendation,
            oxygen
        )

    # ======================================================
    # RIGHT PANEL
    # ======================================================

    with right:

       # =====================================================
       # ACTUAL ALUMINIUM INPUT
       # =====================================================

      if "recommendation" in st.session_state:

          predicted_al = st.session_state["recommendation"]["Predicted_Al"]

          actual_al = st.number_input(
              "Actual Aluminium Used (kg)",
              min_value=0.0,
              value=float(predicted_al),
              step=1.0,
              format="%.1f",
              key="dashboard_actual_al"
         )

          saving = actual_al - predicted_al

          if saving > 0:
             st.success(f"Potential Saving : {saving:.1f} kg")
          elif saving < 0:
             st.info(f"AI Recommended {abs(saving):.1f} kg more than actual")
          else:
             st.success("Perfect! Actual addition matches AI recommendation.")

    # ======================================================
    # FOOTER
    # ======================================================

    st.markdown("---")

    st.caption(
        "🏭 Jindal Steel | AI-Based Aluminium Addition Optimization System | Version 2.0"
    )