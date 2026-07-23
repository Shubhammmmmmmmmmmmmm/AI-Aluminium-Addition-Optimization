import streamlit as st
from datetime import datetime

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

def header(selected_heat):
    # st.write(selected_heat.index.tolist())
    current_time = datetime.now().strftime(
        "%d %b %Y | %I:%M:%S %p"
    )

    st.markdown(
        f"""
<div style="
background:linear-gradient(90deg,#071E3D,#1F4287,#278EA5);
padding:20px;
border-radius:18px;
box-shadow:0px 6px 18px rgba(0,0,0,0.45);
">

<h1 style="
color:white;
margin-bottom:5px;
">
🏭 JINDAL STEEL 
</h1>

<h3 style="
color:#E8F6FF;
margin-top:0px;
margin-bottom:15px;
">
AI Based Aluminium Optimization System
</h3>

<hr style="border:1px solid #5BC0EB;">

<table width="100%">

<tr>
<td>
<b style="color:white;">AI Model :</b><br>
<span style="color:#00E5FF;">Extra Trees</span>
</td>

<td>
<b style="color:white;">System :</b><br>
<span style="color:#00FF66;">🟢 ONLINE</span>
</td>

<td>
<b style="color:white;">Time :</b><br>
<span style="color:white;">{current_time}</span>
</td>

</tr>

</table>

</div>
""",
        unsafe_allow_html=True,
    )