import streamlit as st
import pandas as pd
import plotly.express as px


# ================================================
# Aluminium Saving Dashboard
# ================================================

def saving_dashboard(df):

    st.markdown(
        '<div class="section-title">💰 Aluminium & Cost Saving Analysis</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    # =====================================================
    # LEFT
    # =====================================================

    with left:

        plot_df = df.tail(40).copy()

        if "Predicted_Al" not in plot_df.columns:

            plot_df["Predicted_Al"] = plot_df["Total_Al_LRF_kg"]

        plot_df["Saving_kg"] = (

            plot_df["Total_Al_LRF_kg"]

            -

            plot_df["Predicted_Al"]

        )

        fig = px.line(

            plot_df,

            x=plot_df.index,

            y="Saving_kg",

            markers=True

        )

        fig.update_traces(

            line_color="#00FF88",

            line_width=3

        )

        fig.update_layout(

            template="plotly_dark",

            title="Aluminium Saving / Heat",

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            height=420

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # =====================================================
    # RIGHT
    # =====================================================

    with right:

        plot_df["Saving_INR"] = (

            plot_df["Saving_kg"]

            *410

        )

        fig = px.area(

            plot_df,

            x=plot_df.index,

            y="Saving_INR"

        )

        fig.update_traces(

            line_color="#00d4ff"

        )

        fig.update_layout(

            template="plotly_dark",

            title="Estimated Cost Saving",

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            height=420

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.success(

        f"Estimated Aluminium Saving : {plot_df['Saving_kg'].sum():.1f} kg"

    )

    st.success(

        f"Estimated Cost Saving : ₹ {plot_df['Saving_INR'].sum():,.0f}"

    )