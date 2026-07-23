import streamlit as st

# ==========================================================
# KPI CARD
# ==========================================================

def kpi_card(title, value, subtitle, color="#2563EB", icon="📊"):

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg,#111827,#1F2937);
            border-left:8px solid {color};
            border-radius:18px;
            padding:18px;
            box-shadow:0px 6px 15px rgba(0,0,0,0.40);
            height:155px;
        ">

        <div style="font-size:18px;color:#CBD5E1;">
            {icon} {title}
        </div>

        <div style="
            font-size:34px;
            color:white;
            font-weight:bold;
            margin-top:10px;
        ">
            {value}
        </div>

        <div style="
            color:#9CA3AF;
            margin-top:18px;
            font-size:14px;
        ">
            {subtitle}
        </div>

        </div>
        """,
        unsafe_allow_html=True,)


# ==========================================================
# KPI ROW
# ==========================================================

def show_kpis(selected_heat, recommendation):

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        kpi_card(
            "Heat Number",
            selected_heat.get("Batch Number", "MANUAL HEAT"),
            "Current Heat",
            "#3B82F6",
            "🔥"
        )

    with c2:
        kpi_card(
            "Steel Grade",
            selected_heat.get("GRADE", "-"),
            "Running Grade",
            "#10B981",
            "🏭"
        )

    with c3:
        kpi_card(
            "Temperature",
            f"{selected_heat.get("LIFTING TEMP_LRF", 0):.0f} °C",
            "LRF Lifting Temp",
            "#F59E0B",
            "🌡"
        )

    with c4:
        kpi_card(
            "AI Prediction",
            f"{recommendation['Predicted_Al']:.2f} kg",
            "Recommended Aluminium",
            "#8B5CF6",
            "🤖"
        )

    with c5:
        kpi_card(
             "Recovery",
             f"{recommendation['Recovery']:.1f} %",
             "Predicted Recovery",
             "#22C55E",
             "📈"

        )