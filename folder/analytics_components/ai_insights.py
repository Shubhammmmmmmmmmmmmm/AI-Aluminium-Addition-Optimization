import streamlit as st


def ai_insights(df):

    st.markdown(
        '<div class="section-title">🤖 AI Executive Insights</div>',
        unsafe_allow_html=True
    )

    highest_grade = (

        df.groupby("GRADE")["Total_Al_LRF_kg"]

        .mean()

        .idxmax()

    )

    lowest_grade = (

        df.groupby("GRADE")["Total_Al_LRF_kg"]

        .mean()

        .idxmin()

    )

    avg_al = df["Total_Al_LRF_kg"].mean()

    max_al = df["Total_Al_LRF_kg"].max()

    min_al = df["Total_Al_LRF_kg"].min()

    c1,c2,c3 = st.columns(3)

    with c1:

        st.markdown(f"""

<div class="glass-card">

### 🏭 Steel Grade Analysis

**Highest Aluminium Grade**

{highest_grade}

<br><br>

**Lowest Aluminium Grade**

{lowest_grade}

</div>

""",unsafe_allow_html=True)

    with c2:

        st.markdown(f"""

<div class="glass-card">

### 📈 Consumption Analysis

Average Aluminium

# {avg_al:.1f} kg

Maximum

{max_al:.1f} kg

Minimum

{min_al:.1f} kg

</div>

""",unsafe_allow_html=True)

    with c3:

        st.markdown("""

<div class="glass-card">

### 💡 AI Recommendation

✅ Optimize high Al grades

✅ Reduce slag carryover

✅ Maintain reducing slag

✅ Maintain proper argon stirring

✅ Improve aluminium recovery

</div>

""",unsafe_allow_html=True)