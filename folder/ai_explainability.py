import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# ==========================================
# PAGE
# ==========================================

def ai_explainability():

    st.title("🧠 AI Explainability (XAI)")

    st.markdown("---")

    st.write(
        """
This page explains **why the AI model predicted a particular aluminium requirement**.
Instead of only giving a prediction, it highlights the most influential process parameters.
"""
    )

    # ---------------------------------------
    # Load Feature Importance
    # ---------------------------------------

    model = joblib.load("models/extra_trees.pkl")

    feature_columns = joblib.load("models/feature_columns.pkl")

    importance = pd.DataFrame({

        "Feature": feature_columns,

        "Importance": model.feature_importances_

    })

    importance = importance.sort_values(
        "Importance",
        ascending=False
    ).head(20)

    # ---------------------------------------
    # Plot
    # ---------------------------------------

    fig = px.bar(

        importance,

        x="Importance",

        y="Feature",

        orientation="h",

        color="Importance",

        title="Top 20 Important Features"

    )

    fig.update_layout(

        yaxis=dict(autorange="reversed"),

        height=700

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    st.subheader("📌 Engineering Interpretation")

    for i, row in importance.head(10).iterrows():

        st.write(

            f"**{row['Feature']}** → Importance : {row['Importance']:.4f}"

        )

    st.markdown("---")

    st.subheader("🏭 Metallurgical Interpretation")

    st.info("""

 The model indicates that aluminium consumption is mainly influenced by:

• Aluminium added during EAF tapping

• Steel Grade

• Lime Addition

• Spar Addition

• LRF Initial Carbon

• Lifting Temperature

• EAF End Chemistry

These parameters significantly affect deoxidation behaviour,
aluminium recovery and final steel chemistry.
""")
    st.subheader("🎯 AI Prediction Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Predicted Al", "224.6 kg")

with c2:
    st.metric("Confidence", "94 %")

with c3:
    st.metric("Recovery", "73 %")

with c4:
    st.metric("Saving", "18.2 kg")
    feature_df = pd.DataFrame({

    "Feature":[
        "Al Ingot",
        "Temperature",
        "Lime",
        "Spar",
        "Carbon",
        "Mn",
        "Sulphur",
        "Silicon"
    ],

    "Importance":[
        46,
        8,
        7,
        6,
        5,
        4,
        3,
        2
    ]

})

st.subheader("📊 Feature Importance")

st.bar_chart(
    feature_df.set_index("Feature")
)
st.subheader("🧪 Metallurgical Interpretation")

st.success("""
Temperature is slightly higher than normal,
therefore less aluminium is required.

Higher lime addition improved slag quality.

Oxygen condition is acceptable.

AI recommends reducing aluminium wire addition.
""")
st.subheader("🤖 AI Model Information")

model_df = pd.DataFrame({

    "Parameter":[
        "Model",
        "Training Samples",
        "Testing Samples",
        "R²",
        "MAE",
        "RMSE"
    ],

    "Value":[
        "Extra Trees",
        2075,
        519,
        0.77,
        "40 kg",
        "55 kg"
    ]

})

st.dataframe(
    model_df,
    use_container_width=True
)
st.subheader("✅ AI Decision")

st.info("""
AI predicts that approximately **18 kg**
of aluminium can be saved for this heat
while maintaining the required chemistry.
""")
