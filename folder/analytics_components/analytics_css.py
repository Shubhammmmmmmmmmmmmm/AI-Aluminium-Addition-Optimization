import streamlit as st


def load_css():

    st.markdown("""

<style>

/* ==========================================
BACKGROUND
========================================== */

.stApp{
    background:#081a3a;
}

/* ==========================================
SECTION TITLE
========================================== */

.analytics-title{
    font-size:44px;
    font-weight:800;
    color:#12d8ff;
    margin-bottom:0px;
    text-shadow:0 0 12px rgba(18,216,255,.45);
}

.analytics-subtitle{
    color:#9fb4d1;
    font-size:16px;
    margin-top:-10px;
    margin-bottom:30px;
}

/* ==========================================
GLASS CARD
========================================== */

.glass-card{

background:rgba(20,32,58,.92);

border:1px solid rgba(0,212,255,.22);

border-radius:18px;

padding:22px;

box-shadow:
0 0 12px rgba(0,212,255,.08),
0 10px 25px rgba(0,0,0,.45);

transition:.35s;

}

.glass-card:hover{

transform:translateY(-4px);

box-shadow:

0 0 18px rgba(0,212,255,.25),

0 0 35px rgba(0,212,255,.12);

}

/* ==========================================
KPI
========================================== */

.kpi-title{

font-size:12px;

font-weight:700;

letter-spacing:1px;

color:#93A8C8;

text-transform:uppercase;

}

.kpi-value{

font-size:42px;

font-weight:800;

color:#82E9FF;

margin-top:8px;

}

.kpi-unit{

font-size:18px;

color:white;

}

/* ==========================================
SECTION HEADER
========================================== */

.section-title{

font-size:30px;

font-weight:700;

color:white;

margin-top:15px;

margin-bottom:15px;

}

/* ==========================================
PLOTLY
========================================== */

.js-plotly-plot{

border-radius:16px;

overflow:hidden;

}

/* ==========================================
DATAFRAME
========================================== */

[data-testid="stDataFrame"]{

border-radius:15px;

overflow:hidden;

}

/* ==========================================
METRIC
========================================== */

[data-testid="metric-container"]{

background:#12264A;

border-radius:18px;

padding:18px;

border:1px solid rgba(0,212,255,.15);

}

/* ==========================================
SCROLL BAR
========================================== */

::-webkit-scrollbar{

width:8px;

}

::-webkit-scrollbar-thumb{

background:#0fd6ff;

border-radius:50px;

}

</style>

""",unsafe_allow_html=True)