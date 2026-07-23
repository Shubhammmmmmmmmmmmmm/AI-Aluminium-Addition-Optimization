import streamlit as st

# ===========================================================
# AI OPERATOR CONSOLE
# ===========================================================

def operator_console(rec):

    st.markdown("""
<div style="background:#111827;
border-radius:18px;
padding:22px;
border:2px solid #2563EB;
box-shadow:0px 8px 18px rgba(0,0,0,0.40);">

<h2 style="color:#38BDF8;">
🤖 AI OPERATOR CONSOLE
</h2>

<hr>

<h3 style="color:#22C55E;">

Recommended Charging Practice

</h3>

<table width="100%">

<tr>

<td><b>Al Ingot</b></td>

<td style="color:#FFD54F;"><b>180 kg</b></td>

</tr>

<tr>

<td><b>Al Shots</b></td>

<td style="color:#FFD54F;"><b>40 kg</b></td>

</tr>

<tr>

<td><b>Al Wire</b></td>

<td style="color:#FFD54F;"><b>18 kg</b></td>

</tr>

</table>

<hr>

<table width="100%">

<tr>

<td>Expected Final Al</td>

<td><b>0.031 %</b></td>

</tr>

<tr>

<td>Recovery</td>

<td><b>93 %</b></td>

</tr>

<tr>

<td>AI Confidence</td>

<td><b>94 %</b></td>

</tr>

<tr>

<td>Saving</td>

<td style="color:#22C55E;"><b>18 kg</b></td>

</tr>

<tr>

<td>Risk</td>

<td style="color:#22C55E;"><b>LOW 🟢</b></td>

</tr>

</table>

</div>

""",unsafe_allow_html=True)
  