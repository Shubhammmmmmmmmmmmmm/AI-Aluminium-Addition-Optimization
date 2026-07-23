import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ==========================================================
# LIVE PROCESS TRENDS
# ==========================================================

def live_trends(selected_heat,recommendation,oxygen):

    np.random.seed(42)

    x = list(range(1, 31))

    # Sample live data (replace with real plant data later)
    temperature = np.linspace(

    selected_heat["TEMP OPENING_LRF"],

    selected_heat["LIFTING TEMP_LRF"],

    30

  )
    oxygen = np.linspace(

    selected_heat["Mean_Oxygen"],

    120,

    30

  )
    prediction = recommendation["Predicted_Al"]

    aluminium = np.linspace(
    prediction - 35,
    prediction,
    30
  )

    col1, col2 = st.columns(2)

    # ======================================================
    # Temperature Trend
    # ======================================================

    with col1:

        fig1 = go.Figure()

        fig1.add_trace(
            go.Scatter(
                x=x,
                y=temperature,
                mode="lines",
                name="Temperature",
                line=dict(color="#00E5FF", width=3)
            )
        )

        fig1.update_layout(
            title="🌡 Temperature Trend",
            height=320,
            paper_bgcolor="#0B1220",
            plot_bgcolor="#111827",
            font=dict(color="white"),
            xaxis_title="Time",
            yaxis_title="°C"
        )

        st.plotly_chart(fig1, use_container_width=True)

    # ======================================================
    # Oxygen Trend
    # ======================================================

    with col2:

        fig2 = go.Figure()

        fig2.add_trace(
            go.Scatter(
                x=x,
                y=oxygen,
                mode="lines",
                name="Oxygen",
                line=dict(color="#F59E0B", width=3)
            )
        )

        fig2.update_layout(
            title="🫧 Oxygen Trend",
            height=320,
            paper_bgcolor="#0B1220",
            plot_bgcolor="#111827",
            font=dict(color="white"),
            xaxis_title="Time",
            yaxis_title="ppm"
        )

        st.plotly_chart(fig2, use_container_width=True)

    # ======================================================
    # Aluminium Trend
    # ======================================================

    fig3 = go.Figure()

    fig3.add_trace(
        go.Scatter(
            x=x,
            y=aluminium,
            mode="lines+markers",
            name="Actual Al",
            line=dict(color="#22C55E", width=3)
        )
    )

    fig3.add_hline(
        y=recommendation["Predicted_Al"],
        line_dash="dash",
        line_color="red",
        annotation_text="AI Recommendation"
    )

    fig3.update_layout(
        title="🤖 Aluminium Consumption Trend",
        height=350,
        paper_bgcolor="#0B1220",
        plot_bgcolor="#111827",
        font=dict(color="white"),
        xaxis_title="Heat Sequence",
        yaxis_title="kg"
    )

    st.plotly_chart(fig3, use_container_width=True)