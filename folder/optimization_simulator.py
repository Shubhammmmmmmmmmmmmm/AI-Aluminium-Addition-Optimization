import streamlit as st
import pandas as pd

from utils.prediction import predict_heat
from utils.recommendation import generate_recommendation

df = pd.read_csv("clean_data/clean_dataset.csv")
def optimization_simulator():
    st.title("⚙ AI Optimization Simulator")

    st.caption(
        "Simulate different LRF process conditions and compare current plant practice with AI recommendations."
    )

    st.markdown("---")

    # ==========================================
    # Heat Selection
    # ==========================================

    st.subheader("🔥 Heat Selection")

    c1, c2 = st.columns([4, 1])

    with c1:
        heat = st.selectbox(
            "Select Historical Heat",
            df.index
        )

    with c2:
        st.write("")
        st.write("")
        st.button(
            "🔄 Load",
            use_container_width=True
        )

    selected = df.iloc[[heat]]

    st.markdown("---")

    st.subheader("⚙ Editable Process Parameters")

    st.info(
        "Modify the process parameters and click RUN AI OPTIMIZATION."
    )

    left, right = st.columns(2)

    with left:

        temp = st.number_input(
            "Temperature (°C)",
            value=float(selected["LIFTING TEMP_LRF"].iloc[0])
        )

        oxygen = st.number_input(
            "Oxygen",
            value=float(selected["OXY_EAF"].iloc[0])
        )

        carbon = st.number_input(
            "Carbon (%)",
            value=float(selected["LRF_Final_Chemistry_C"].iloc[0])
        )

        silicon = st.number_input(
            "Silicon (%)",
            value=float(selected["Final_SI"].iloc[0])
        )

    with right:

        manganese = st.number_input(
            "Manganese (%)",
            value=float(selected["LRF_Final_Chemistry_MN"].iloc[0])
        )

        lime = st.number_input(
            "Lime (kg)",
            value=float(selected["LIME_LRF"].iloc[0])
        )

        spar = st.number_input(
            "Spar (kg)",
            value=float(selected["SPAR"].iloc[0])
        )

        argon = st.slider(
            "Argon Stirring Time (min)",
            5,
            25,
            15
        )

    modified = selected.copy()

    modified["LIFTING TEMP_LRF"] = temp
    modified["OXY_EAF"] = oxygen
    modified["LRF_Final_Chemistry_C"] = carbon
    modified["Final_SI"] = silicon
    modified["LRF_Final_Chemistry_MN"] = manganese
    modified["LIME_LRF"] = lime
    modified["SPAR"] = spar

    st.markdown("---")

    run = st.button(
        "🚀 RUN AI OPTIMIZATION",
        use_container_width=True
    )

    if run:

        prediction = predict_heat(modified)

        recommendation = generate_recommendation(prediction)
        st.markdown("---")

        st.subheader("🤖 AI Optimization Result")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Predicted Al",
                f"{recommendation['Predicted_Al']:.1f} kg"
            )

        with c2:
            st.metric(
                "Saving",
                f"{recommendation['Saving']:.1f} kg"
            )

        with c3:
            st.metric(
                "Recovery",
                f"{recommendation['Recovery']} %"
            )

        with c4:
            st.metric(
                "Confidence",
                f"{recommendation['Confidence']} %"
            )

        st.markdown("---")

        st.subheader("📊 Current Plant vs AI Optimized")

        current_al = (
            float(selected["al ingot_kg__during_EAF_tapping"].iloc[0]) +
            float(selected["AL SHOTS_LRF_kg"].iloc[0]) +
            float(selected["Al_wire_kg"].iloc[0])
        )

        ai_al = recommendation["Predicted_Al"]

        saving = max(current_al - ai_al, 0)

        c1, c2, c3 = st.columns(3)

        with c1:
            st.info(f"""
### 🏭 Current Plant

**Aluminium Used**

### {current_al:.1f} kg
""")

        with c2:
            st.success(f"""
### 🤖 AI Optimized

**Recommended**

### {ai_al:.1f} kg
""")

        with c3:
            st.warning(f"""
### 💰 Saving

**Expected Saving**

### {saving:.1f} kg
""")

        st.markdown("---")

        compare = pd.DataFrame(
            {
                "Aluminium (kg)": [
                    current_al,
                    ai_al
                ]
            },
            index=[
                "Current Plant",
                "AI Optimized"
            ]
        )

        st.subheader("📈 Aluminium Comparison")

        st.bar_chart(compare)
        st.markdown("---")

        st.subheader("💵 Estimated Cost Saving")

        aluminium_price = st.number_input(
            "Aluminium Price (₹/kg)",
            value=240.0
        )

        saving_rupees = saving * aluminium_price

        monthly = saving_rupees * 250

        yearly = monthly * 12

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Saving / Heat",
                f"₹ {saving_rupees:,.0f}"
            )

        with c2:
            st.metric(
                "Monthly Saving",
                f"₹ {monthly:,.0f}"
            )

        with c3:
            st.metric(
                "Annual Saving",
                f"₹ {yearly:,.0f}"
            )

        st.markdown("---")

        if saving > 15:

            st.success(f"""
### 🤖 AI Recommendation

✔ Reduce aluminium addition by approximately **{saving:.1f} kg**

✔ Maintain reducing slag practice

✔ Continue proper argon stirring

✔ Oxygen level is acceptable

✔ Estimated recovery : **{recommendation['Recovery']} %**

✔ Model confidence : **{recommendation['Confidence']} %**
""")

        else:

            st.info(f"""
### 🤖 AI Recommendation

Current aluminium practice is already close to optimum.

Only minor optimization is possible.

Expected recovery : **{recommendation['Recovery']} %**

Model confidence : **{recommendation['Confidence']} %**
""")