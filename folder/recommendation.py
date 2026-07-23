import streamlit as st
import pandas as pd

from utils.prediction import predict_heat
from utils.recommendation import generate_recommendation

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("clean_data/clean_dataset.csv")


# ==========================================
# PAGE
# ==========================================

def recommendation():

    st.title("🤖 AI Recommendation Center")

    st.markdown("---")

    # ------------------------------------
    # Heat Selection
    # ------------------------------------

    heat_no = st.slider(

        "Select Heat",

        0,

        len(df)-1,

        0

    )

    heat = df.iloc[[heat_no]]

    predicted = predict_heat(heat)

    rec = generate_recommendation(predicted)

    actual = heat["Total_Al_LRF_kg"].iloc[0]

    # ------------------------------------
    # KPI
    # ------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Actual Al",
        f"{actual:.1f} kg"
    )

    c2.metric(
        "AI Prediction",
        f"{rec['Predicted_Al']:.1f} kg"
    )

    c3.metric(
        "Potential Saving",
        f"{actual-rec['Predicted_Al']:.1f} kg"
    )

    c4.metric(
        "Confidence",
        f"{rec['Confidence']} %"
    )

    st.markdown("---")

    # ------------------------------------
    # Recommendation Table
    # ------------------------------------

    st.subheader("🏭 Recommended Aluminium Addition")

    recommendation_df = pd.DataFrame({

        "Material":[

            "Al Ingot",

            "Al Shots",

            "Al Wire"

        ],

        "Recommended Quantity":[

            rec["Ingot"],

            rec["Shots"],

            rec["Wire"]

        ]

    })

    st.dataframe(

        recommendation_df,

        use_container_width=True,

        hide_index=True

    )

    st.markdown("---")

    # ------------------------------------
    # Operator Guideline
    # ------------------------------------

    st.subheader("👨‍🏭 Operator Guideline")

    saving = actual - rec["Predicted_Al"]

    if saving > 15:

        st.success("""
### Recommendation

✅ Aluminium can safely be reduced.

Maintain good slag practice.

Maintain proper argon stirring.

Avoid unnecessary wire feeding.

Monitor final chemistry before tapping.
""")

    elif saving > 5:

        st.info("""
### Recommendation

Small optimisation is possible.

Follow normal LRF practice.

Check oxygen level before final trimming.
""")

    else:

        st.warning("""
### Recommendation

Current practice is already close to optimum.

No major reduction is recommended.
""")

    st.markdown("---")

    # ------------------------------------
    # Cost Saving
    # ------------------------------------

    st.subheader("💰 Estimated Cost Saving")

    aluminium_price = st.number_input(

        "Aluminium Price (₹/kg)",

        value=250

    )

    saving_rupees = saving * aluminium_price

    st.metric(

        "Estimated Saving",

        f"₹ {saving_rupees:,.0f}"

    )

    st.markdown("---")

    st.subheader("📌 AI Remarks")

    st.info(f"""

• Expected Recovery : {rec['Recovery']} %

• Expected Final Aluminium : Stable

• AI Confidence : {rec['Confidence']} %

• Suggested Practice :

   • 180 kg Ingot

   • 40 kg Shots

   • {rec['Wire']:.1f} kg Wire

""")
    