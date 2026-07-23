import streamlit as st

def prediction_panel(recommendation):

    st.subheader("🤖 AI Prediction")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Predicted Al",
            f"{recommendation['Predicted_Al']:.1f} kg"
        )

        st.metric(
            "Recovery",
            f"{recommendation['Recovery']} %"
        )

    with c2:

        st.metric(
            "Confidence",
            f"{recommendation['Confidence']} %"
        )

        st.metric(
            "Saving",
            f"{recommendation['Saving']:.1f} kg"
        )

    st.progress(recommendation["Confidence"]/100)

    if recommendation["Saving"] > 15:

        st.success("✅ High Saving Opportunity")

    elif recommendation["Saving"] > 5:

        st.warning("⚠ Medium Saving Opportunity")

    else:

        st.info("ℹ Aluminium already optimized")