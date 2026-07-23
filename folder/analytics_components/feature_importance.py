import streamlit as st
import plotly.express as px
import pandas as pd


def feature_importance():

    st.markdown(
        '<div class="section-title">🧠 AI Feature Importance</div>',
        unsafe_allow_html=True
    )

    # ============================================
    # Replace these values later with your
    # Extra Trees feature importance CSV
    # ============================================

    feature_df = pd.DataFrame({

        "Feature":[

            "Al Ingot During EAF",

            "Steel Grade",

            "Lime",

            "Opening Temperature",

            "Spar",

            "Lifting Temperature",

            "Carbon",

            "Silicon",

            "Sulphur",

            "Nitrogen"

        ],

        "Importance":[

            0.46,

            0.12,

            0.08,

            0.07,

            0.05,

            0.04,

            0.03,

            0.025,

            0.018,

            0.015

        ]

    })

    fig = px.bar(

        feature_df,

        y="Feature",

        x="Importance",

        orientation="h",

        color="Importance",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        height=550,

        coloraxis_showscale=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )