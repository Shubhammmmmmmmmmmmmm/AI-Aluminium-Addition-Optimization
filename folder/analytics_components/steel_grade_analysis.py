import streamlit as st
import plotly.express as px


def steel_grade_analysis(df):

    st.markdown(
        '<div class="section-title">🏭 Average Aluminium by Steel Grade</div>',
        unsafe_allow_html=True
    )

    grade = (

        df.groupby("GRADE")["Total_Al_LRF_kg"]

        .mean()

        .sort_values(ascending=False)

        .head(15)

        .reset_index()

    )

    fig = px.bar(

        grade,

        y="GRADE",

        x="Total_Al_LRF_kg",

        orientation="h",

        color="Total_Al_LRF_kg",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        template="plotly_dark",

        height=550,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        coloraxis_showscale=False,

        margin=dict(

            l=20,

            r=20,

            t=40,

            b=20

        )

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    highest = grade.iloc[0]

    lowest = grade.iloc[-1]

    st.info(

        f"""
Highest Aluminium Consumption Grade : **{highest['GRADE']}**

Average Aluminium : **{highest['Total_Al_LRF_kg']:.1f} kg**

Lowest (Top 15) Grade : **{lowest['GRADE']}**

Average Aluminium : **{lowest['Total_Al_LRF_kg']:.1f} kg**
"""
    )