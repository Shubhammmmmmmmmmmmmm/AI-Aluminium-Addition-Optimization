import streamlit as st

def analytics_kpis(df):

    # ============================
    # Calculate KPI Values
    # ============================

    total_heats = len(df)
    total_grades = df["GRADE"].nunique()
    avg_al = df["Total_Al_LRF_kg"].mean()

    # Your actual model performance
    model_accuracy = "R² = 0.77"

    c1, c2, c3, c4 = st.columns(4)

    # ==========================================
    # KPI 1
    # ==========================================

    with c1:
        st.markdown(f"""
<div class="glass-card">
    <div class="kpi-title">
        🔥 TOTAL HEATS
    </div>
    <div class="kpi-value">
        {total_heats:,}
    </div>
</div>
""", unsafe_allow_html=True)

    # ==========================================
    # KPI 2
    # ==========================================

    with c2:
        st.markdown(f"""
<div class="glass-card">
    <div class="kpi-title">
        🏭 STEEL GRADES
    </div>
    <div class="kpi-value">
        {total_grades}
    </div>
</div>
""", unsafe_allow_html=True)

    # ==========================================
    # KPI 3
    # ==========================================

    with c3:
        st.markdown(f"""
<div class="glass-card">
    <div class="kpi-title">
        ⚖ AVG AL CONSUMPTION
    </div>
    <div class="kpi-value">
        {avg_al:.1f}
        <span class="kpi-unit">kg</span>
    </div>
</div>
""", unsafe_allow_html=True)

    # ==========================================
    # KPI 4
    # ==========================================

    with c4:
        st.markdown(f"""
<div class="glass-card">
    <div class="kpi-title">
        🤖 AI MODEL
    </div>
    <div class="kpi-value" style="font-size:28px;">
        {model_accuracy}
    </div>
</div>
""", unsafe_allow_html=True)

    st.write("")