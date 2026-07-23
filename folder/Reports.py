# import streamlit as st
# import pandas as pd
# from datetime import datetime

# # ============================================
# # Load Dataset
# # ============================================

# df = pd.read_csv("clean_data/clean_dataset.csv")


# def reports():

#     st.title("📄 AI Report Center")

#     st.caption(
#         "Generate and download AI aluminium optimization reports."
#     )

#     st.markdown("---")

#     # ============================================
#     # REPORT SOURCE
#     # ============================================

#     st.subheader("📂 Report Source")

#     source = st.radio(

#         "",

#         [

#            "📌 Current Prediction",

#            "📚 Historical Heat"

#         ],

#         horizontal=True

#     )

#    # ============================================
#    # CURRENT PREDICTION
#    # ============================================

#     if source == "📌 Current Prediction":

#        if st.session_state.get("prediction_done", False):

#           recommendation = st.session_state["recommendation"]

#           selected = pd.DataFrame([{

#              "Batch Number": "MANUAL HEAT",

#              "GRADE": st.session_state.get("grade", "Manual"),

#              "LIFTING TEMP_LRF": st.session_state.get("temperature", 0),
  
#              "Total_Al_LRF_kg": recommendation["Predicted_Al"],

#              "LIME_LRF": st.session_state.get("lime", 0),

#              "SPAR": st.session_state.get("spar", 0),

#              "LRF_Final_Chemistry_C": st.session_state.get("carbon", 0),

#              "Final_SI": st.session_state.get("silicon", 0)

#            }])

#          else:

#           st.warning("⚠ No prediction available. Please generate a prediction first.")

#           return

#      # ============================================
#      # HISTORICAL DATA
#      # ============================================

#     else:

#       heat = st.selectbox(

#         "Select Historical Heat",

#         df.index

#     )

#     selected = df.iloc[[heat]]

#     st.subheader("🏭 Heat Information")

#     c1, c2, c3 = st.columns(3)

#     with c1:

#         st.metric(
#             "Grade",
#             selected["GRADE"].iloc[0]
#         )

#     with c2:

#         st.metric(
#             "Temperature",
#             f"{selected['LIFTING TEMP_LRF'].iloc[0]} °C"
#         )

#     with c3:

#         st.metric(
#             "Total Aluminium",
#             f"{selected['Total_Al_LRF_kg'].iloc[0]:.1f} kg"
#         )

#     st.markdown("---")

#     # ============================================
#     # AI Recommendation Summary
#     # ============================================

#     st.subheader("🤖 AI Recommendation Summary")

#     st.success("""

# ✔ Reduce unnecessary aluminium trimming.

# ✔ Maintain reducing slag practice.

# ✔ Improve aluminium recovery.

# ✔ Maintain proper argon stirring.

# ✔ Monitor oxygen before final aluminium addition.

# ✔ Follow AI recommendation before aluminium wire feeding.

# """)

#     st.markdown("---")

#     # ============================================
#     # Report Preview
#     # ============================================

#     st.subheader("📑 Report Preview")

#     preview = pd.DataFrame({

#         "Parameter": [

#             "Grade",

#             "Temperature",

#             "Total Aluminium",

#             "Lime",

#             "Spar",

#             "Carbon",

#             "Silicon"

#         ],

#         "Value": [

#             selected["GRADE"].iloc[0],

#             selected["LIFTING TEMP_LRF"].iloc[0],

#             selected["Total_Al_LRF_kg"].iloc[0],

#             selected["LIME_LRF"].iloc[0],

#             selected["SPAR"].iloc[0],

#             selected["LRF_Final_Chemistry_C"].iloc[0],

#             selected["Final_SI"].iloc[0]

#         ]

#     })

#     st.dataframe(
#         preview,
#         use_container_width=True
#     )

#     st.markdown("---")

#     # ============================================
#     # Download Section
#     # ============================================

#     st.subheader("⬇ Download Reports")

#     csv = preview.to_csv(index=False).encode("utf-8")

#     c1, c2, c3 = st.columns(3)

#     with c1:

#         st.download_button(

#             "📄 Download CSV",

#             csv,

#             file_name="AI_Report.csv",

#             mime="text/csv"

#         )

#     with c2:

#         st.download_button(

#             "📊 Download Excel",

#             csv,

#             file_name="AI_Report.xls",

#             mime="application/vnd.ms-excel"

#         )

#     with c3:

#         st.button(
#             "📑 Generate PDF"
#         )

#     st.markdown("---")

#     # ============================================
#     # Report Details
#     # ============================================

#     st.subheader("📋 Report Information")

#     st.info(f"""

# Report Generated :

# **{datetime.now().strftime("%d-%m-%Y %H:%M")}**

# Project :

# **AI Based Aluminium Addition Optimization**

# Plant :

# **JINDAL STEEL RAIGARH**

# Department :

# **SMS - LRF**

# AI Model :

# **Extra Trees Regressor**

# Prediction Accuracy :

# **69 % (R² Score)**

# """)

#     st.markdown("---")

#     st.success("""

# ### Final Recommendation

# ✔ Continue AI Based Aluminium Prediction.

# ✔ Improve Aluminium Recovery.

# ✔ Minimize Aluminium Trimming.

# ✔ Maintain Reducing Slag Practice.

# ✔ Continue Monitoring Oxygen Level.

# ✔ Estimated Aluminium Saving :

# **18 kg / Heat**

# """)
    

    ####gemini trial#####
import streamlit as st
import pandas as pd
from datetime import datetime

# ============================================
# Load Dataset
# ============================================
df = pd.read_csv("clean_data/clean_dataset.csv")

def reports():
    st.title("📄 AI Report Center")
    st.caption(
        "Generate and download AI aluminium optimization reports."
    )
    st.markdown("---")

    # ============================================
    # REPORT SOURCE
    # ============================================
    st.subheader("📂 Report Source")
    source = st.radio(
        "",
        [
           "📌 Current Prediction",
           "📚 Historical Heat"
        ],
        horizontal=True
    )

    # ============================================
    # CURRENT PREDICTION
    # ============================================
    if source == "📌 Current Prediction":
        if st.session_state.get("prediction_done", False):
            recommendation = st.session_state["recommendation"]
            selected = pd.DataFrame([{
                "Batch Number": "MANUAL HEAT",
                "GRADE": st.session_state.get("grade", "Manual"),
                "LIFTING TEMP_LRF": st.session_state.get("temperature", 0),
                "Total_Al_LRF_kg": recommendation["Predicted_Al"],
                "LIME_LRF": st.session_state.get("lime", 0),
                "SPAR": st.session_state.get("spar", 0),
                "LRF_Final_Chemistry_C": st.session_state.get("carbon", 0),
                "Final_SI": st.session_state.get("silicon", 0)
            }])
        else:
            st.warning("⚠ No prediction available. Please generate a prediction first.")
            return

    # ============================================
    # HISTORICAL DATA
    # ============================================
    else:
        heat = st.selectbox(
            "Select Historical Heat",
            df.index
        )
        selected = df.iloc[[heat]]

    st.subheader("🏭 Heat Information")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Grade",
            selected["GRADE"].iloc[0]
        )

    with c2:
        st.metric(
            "Temperature",
            f"{selected['LIFTING TEMP_LRF'].iloc[0]} °C"
        )

    with c3:
        st.metric(
            "Total Aluminium",
            f"{selected['Total_Al_LRF_kg'].iloc[0]:.1f} kg"
        )

    st.markdown("---")

    # ============================================
    # AI Recommendation Summary
    # ============================================
    st.subheader("🤖 AI Recommendation Summary")
    st.success("""
✔ Reduce unnecessary aluminium trimming.
✔ Maintain reducing slag practice.
✔ Improve aluminium recovery.
✔ Maintain proper argon stirring.
✔ Monitor oxygen before final aluminium addition.
✔ Follow AI recommendation before aluminium wire feeding.
""")
    st.markdown("---")

    # ============================================
    # Report Preview
    # ============================================
    st.subheader("📑 Report Preview")
    preview = pd.DataFrame({
        "Parameter": [
            "Grade",
            "Temperature",
            "Total Aluminium",
            "Lime",
            "Spar",
            "Carbon",
            "Silicon"
        ],
        "Value": [
            selected["GRADE"].iloc[0],
            selected["LIFTING TEMP_LRF"].iloc[0],
            selected["Total_Al_LRF_kg"].iloc[0],
            selected["LIME_LRF"].iloc[0],
            selected["SPAR"].iloc[0],
            selected["LRF_Final_Chemistry_C"].iloc[0],
            selected["Final_SI"].iloc[0]
        ]
    })
    st.dataframe(
        preview,
        use_container_width=True
    )
    st.markdown("---")

    # ============================================
    # Download Section
    # ============================================
    st.subheader("⬇ Download Reports")
    csv = preview.to_csv(index=False).encode("utf-8")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.download_button(
            "📄 Download CSV",
            csv,
            file_name="AI_Report.csv",
            mime="text/csv"
        )

    with c2:
        st.download_button(
            "📊 Download Excel",
            csv,
            file_name="AI_Report.xls",
            mime="application/vnd.ms-excel"
        )

    with c3:
        st.button(
            "📑 Generate PDF"
        )

    st.markdown("---")

    # ============================================
    # Report Details
    # ============================================
    st.subheader("📋 Report Information")
    st.info(f"""
Report Generated :
**{datetime.now().strftime("%d-%m-%Y %H:%M")}**
Project :
**AI Based Aluminium Addition Optimization**
Plant :
**JINDAL STEEL RAIGARH**
Department :
**SMS - LRF**
AI Model :
**Extra Trees Regressor**
Prediction Accuracy :
**69 % (R² Score)**
""")
    st.markdown("---")
    st.success("""
### Final Recommendation
✔ Continue AI Based Aluminium Prediction.
✔ Improve Aluminium Recovery.
✔ Minimize Aluminium Trimming.
✔ Maintain Reducing Slag Practice.
✔ Continue Monitoring Oxygen Level.
✔ Estimated Aluminium Saving :
**18 kg / Heat**
""")