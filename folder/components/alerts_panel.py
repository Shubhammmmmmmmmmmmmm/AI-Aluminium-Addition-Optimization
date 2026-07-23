import streamlit as st

def alerts_panel(recommendation):

    st.subheader("🚨 AI Alerts")

    if recommendation["Saving"] > 15:

        st.error("High Aluminium Consumption")

    else:

        st.success("Consumption Normal")

    if recommendation["Recovery"] < 70:

        st.warning("Low Recovery")

    else:

        st.success("Recovery Good")

    if recommendation["Confidence"] > 90:

        st.success("Prediction Reliable")

    else:

        st.info("Check Prediction")