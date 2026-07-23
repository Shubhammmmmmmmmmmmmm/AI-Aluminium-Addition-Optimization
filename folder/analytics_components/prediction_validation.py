import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def prediction_validation(df):

    st.markdown(
        '<div class="section-title">📈 AI Prediction Validation</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([2,1])

    # =====================================================
    # Actual vs Predicted
    # =====================================================

    with left:

        plot_df = df.tail(40).copy()

        # ---------- CURRENT PLACEHOLDER ----------
        # Replace this after 18 June with actual AI prediction column

        if "Predicted_Al" not in plot_df.columns:

            plot_df["Predicted_Al"] = plot_df["Total_Al_LRF_kg"]

        fig = go.Figure()

        fig.add_trace(

            go.Scatter(

                x=plot_df.index,

                y=plot_df["Total_Al_LRF_kg"],

                name="Actual",

                mode="lines+markers",

                line=dict(

                    color="#ff4d4d",

                    width=3

                )

            )

        )

        fig.add_trace(

            go.Scatter(

                x=plot_df.index,

                y=plot_df["Predicted_Al"],

                name="AI Prediction",

                mode="lines",

                line=dict(

                    color="#00d4ff",

                    width=3,

                    dash="dash"

                )

            )

        )

        fig.update_layout(

            template="plotly_dark",

            height=420,

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            margin=dict(l=10,r=10,t=40,b=10),

            title="Actual vs AI Predicted Aluminium"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # =====================================================
    # Error Distribution
    # =====================================================

    with right:

        plot_df["Error"] = (

            plot_df["Total_Al_LRF_kg"]

            -

            plot_df["Predicted_Al"]

        )

        fig2 = go.Figure()

        fig2.add_trace(

            go.Bar(

                x=plot_df.index,

                y=plot_df["Error"],

                marker_color="#00d4ff"

            )

        )

        fig2.update_layout(

            template="plotly_dark",

            height=420,

            title="Prediction Error",

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)"

        )

        st.plotly_chart(

            fig2,

            use_container_width=True

        )