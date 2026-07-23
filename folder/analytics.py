import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from folder.analytics_components.analytics_css import load_css
from folder.analytics_components.analytics_header import analytics_header
from folder.analytics_components.analytics_kpis import analytics_kpis
from folder.analytics_components.prediction_validation import prediction_validation
from folder.analytics_components.steel_grade_analysis import steel_grade_analysis
from folder.analytics_components.saving_dashboard import saving_dashboard
from folder.analytics_components.process_analysis import process_analysis
from folder.analytics_components.feature_importance import feature_importance
from folder.analytics_components.ai_insights import ai_insights
# =====================================================
# PAGE
# =====================================================

def analytics():
    
    load_css()

    analytics_header()
    df = pd.read_csv("clean_data/clean_dataset.csv")

    analytics_kpis(df)
    prediction_validation(df)
    st.markdown("---")
    steel_grade_analysis(df)
    st.markdown("---")

    saving_dashboard(df)

    st.markdown("---")

    process_analysis(df)
    st.markdown("---")

    feature_importance()

    st.markdown("---")

    ai_insights(df)
    st.title("📊 AI Analytics Dashboard")

    st.markdown("---")

    # ---------------------------------------
    # Load Dataset
    # ---------------------------------------

    df = pd.read_csv("clean_data/clean_dataset.csv")

    st.success(f"Dataset Loaded Successfully ({len(df)} heats)")

    # ---------------------------------------
    # KPI
    # ---------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Heats",
        len(df)
    )

    c2.metric(
        "Average Aluminium",
        f"{df['Total_Al_LRF_kg'].mean():.1f} kg"
    )

    c3.metric(
        "Maximum Aluminium",
        f"{df['Total_Al_LRF_kg'].max():.1f} kg"
    )

    c4.metric(
        "Minimum Aluminium",
        f"{df['Total_Al_LRF_kg'].min():.1f} kg"
    )

    st.markdown("---")

    # ======================================
    # Distribution
    # ======================================

    st.subheader("Distribution of Aluminium Consumption")

    fig = px.histogram(
        df,
        x="Total_Al_LRF_kg",
        nbins=30,
        title="Total Aluminium Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ======================================
    # Grade Wise Aluminium
    # ======================================

    st.subheader("Average Aluminium by Steel Grade")

    grade = (

        df.groupby("GRADE")["Total_Al_LRF_kg"]

        .mean()

        .sort_values(ascending=False)

        .reset_index()

    )

    fig = px.bar(

        grade,

        x="GRADE",

        y="Total_Al_LRF_kg",

        color="Total_Al_LRF_kg"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================
    # Temperature
    # ======================================

    st.subheader("Temperature vs Aluminium")

    fig = px.scatter(

        df,

        x="LIFTING TEMP_LRF",

        y="Total_Al_LRF_kg",

        color="GRADE",

        opacity=0.7

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================
    # Correlation
    # ======================================

    st.subheader("Top Correlated Parameters")

    numeric = df.select_dtypes(include="number")

    corr = (

        numeric.corr()["Total_Al_LRF_kg"]

        .sort_values(

            ascending=False

        )

    )

    st.dataframe(

        corr,

        use_container_width=True

    )


########2ND TIME#######
# 