import streamlit as st
import pandas as pd

from utils.prediction import predict_heat
from utils.recommendation import generate_recommendation

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_dataset():
    return pd.read_csv("clean_data/clean_dataset.csv")


@st.cache_data
def load_chemistry_master():
    return pd.read_excel("Final_Grade_Chemistry_Master.xlsx")


@st.cache_data
def load_oxygen_master():
    return pd.read_excel("Grade_Oxygen_Master.xlsx")


df = load_dataset()
chem_master = load_chemistry_master()
oxy_master = load_oxygen_master()


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def get_grade_targets(grade):

    row = chem_master.loc[chem_master["GRADE"] == grade]

    if not row.empty:

        return {

            "C_Target": row.iloc[0]["C_Target"],
            "Mn_Target": row.iloc[0]["Mn_Target"],
            "Si_Target": row.iloc[0]["Si_Target"],
            "Al_Target": row.iloc[0]["Al_Target"]

        }

    return {

        "C_Target": chem_master["C_Target"].median(),
        "Mn_Target": chem_master["Mn_Target"].median(),
        "Si_Target": chem_master["Si_Target"].median(),
        "Al_Target": chem_master["Al_Target"].median()

    }


def get_grade_oxygen(grade):

    row = oxy_master.loc[oxy_master["GRADE"] == grade]

    if not row.empty:

        return row.iloc[0]["Mean_Oxygen"]

    return oxy_master["Mean_Oxygen"].mean()


def calculate_gap(initial, target):

    return target - initial


# =====================================================
# MAIN PAGE
# =====================================================

def prediction():
    st.markdown("""
    <style>

    /* Input Labels */

    label{

        color:#F8FAFC !important;
        font-size:16px !important;
        font-weight:600 !important;

    }

    /* Input Text */

    input{

        color:#111827 !important;
        font-weight:600 !important;

    }

    /* Selectbox Text */

    div[data-baseweb="select"] *{

        color:#111827 !important;

    }
    div[data-testid="stMetricLabel"] p{

      color:#CBD5E1 !important;
      font-size:17px !important;
      font-weight:600 !important;

    }



    div[data-testid="stMetricValue"]{

      color:#FFFFFF !important;
      font-size:38px !important;
      font-weight:700 !important;

    }



    div[data-testid="stMetricDelta"]{

      color:#22C55E !important;
      font-size:18px !important;
      font-weight:600 !important;
    }
      /* -------- Radio Button Text -------- */

  .stRadio label{

      color:#FFFFFF !important;
      font-size:17px !important;
      font-weight:600 !important;

    }

     /* Selected Radio Option */

    div[role="radiogroup"] label[data-checked="true"]{

      color:#38BDF8 !important;
      font-weight:700 !important;

    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
   <h1 style="
   color:white;
   font-size:36px;
   font-weight:800;
   margin-bottom:5px;">
   🤖 AI Aluminium Prediction
   </h1>

   <p style="
   color:#9CA3AF;
   font-size:16px;
   margin-top:0;">
   Predict optimum aluminium requirement using the AI model trained on historical LRF production data.
   </p>
   """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Prediction Mode")

   # Initialize mode once
    if "mode" not in st.session_state:
       st.session_state.mode = "historical"

    col1, col2 = st.columns(2)

    with col1:
         if st.button(
             "📂 Historical Dataset",
             use_container_width=True,
             type="primary" if st.session_state.mode == "historical" else "secondary"
        ):
            st.session_state.mode = "historical"

    with col2:
         if st.button(
             "✍ Manual Heat Entry",
             use_container_width=True,
             type="primary" if st.session_state.mode == "manual" else "secondary"
        ):
            st.session_state.mode = "manual"

    mode = (
        "📂 Historical Dataset"
        if st.session_state.mode == "historical"
        else "✍ Manual Heat Entry"
    )

    st.markdown("---")

    # =====================================================
    # HISTORICAL DATASET
    # =====================================================

    if mode == "📂 Historical Dataset":

        heat_no = st.slider(

            "Select Heat",

            min_value=0,

            max_value=len(df)-1,

            value=0

        )

        heat = df.iloc[[heat_no]]

        st.markdown("""
        <h2 style="
        color:white;
        font-size:24px;
        font-weight:700;">
        📂 Selected Heat Details
         </h2>
        """, unsafe_allow_html=True)

        st.dataframe(

            heat,

            width="stretch",

            height=220,

            hide_index=True

        )

        st.write("")

        predict_btn = st.button(

            "🚀 Predict Aluminium Requirement",

            width="stretch"

        )

        if predict_btn:

            prediction = predict_heat(heat)

            recommendation = generate_recommendation(prediction)

            actual = float(

                heat["Total_Al_LRF_kg"].iloc[0]

            )

            predicted = recommendation["Predicted_Al"]

            saving = actual - predicted

            st.session_state["prediction_done"] = True

            st.session_state["recommendation"] = recommendation

            st.session_state["predicted_al"] = predicted

            st.session_state["manual_heat"] = heat
            st.session_state["dashboard_data"] = {

              "selected_heat": {
                 **manual_heat.iloc[0].to_dict(),

                 "Batch Number": "MANUAL HEAT"
              }, 
              "recommendation": recommendation
          }

            st.markdown("---")

            st.markdown("""
            <h2 style="
            color:white;
            font-size:24px;
            font-weight:700;">
            📊 AI Prediction Result
            </h2>
            """, unsafe_allow_html=True)

            k1, k2, k3, k4 = st.columns(4)

            with k1:

                st.metric(

                    "Predicted Al",

                    f"{predicted:.1f} kg"

                )

            with k2:

                st.metric(

                    "Actual Al",

                    f"{actual:.1f} kg"

                )

            with k3:

                st.metric(

                    "Difference",

                    f"{saving:.1f} kg"

                )

            with k4:

                st.metric(

                    "Confidence",

                    f"{recommendation['Confidence']} %"

                )

            st.markdown("---")

            st.markdown("""
            <h2 style="
            color:white;
            font-size:24px;
            font-weight:700;">
            🏭 AI Recommendation
            </h2>
            """, unsafe_allow_html=True)

            rec_df = pd.DataFrame({

                "Material":[

                    "Al Ingot",

                    "Al Shots",

                    "Al Wire"

                ],

                "Recommended":[

                    recommendation["Ingot"],

                    recommendation["Shots"],

                    recommendation["Wire"]

                ]

            })

            st.dataframe(

                rec_df,

                width="stretch",

                hide_index=True

            )

            st.markdown("---")

            st.subheader("📈 AI vs Actual")

            compare = pd.DataFrame({

                "Parameter":[

                    "Actual Aluminium",

                    "Predicted Aluminium",

                    "Potential Saving"

                ],

                "Value":[

                    round(actual,2),

                    round(predicted,2),

                    round(saving,2)

                ]

            })

            compare["Value"] = compare["Value"].astype(str)

            st.dataframe(

                compare,

                width="stretch",

                hide_index=True

            )

            st.markdown("---")

            st.subheader("🧠 Engineering Interpretation")

            if saving > 0:

                st.success(

                    f"""

AI estimates that this heat could have been produced using approximately **{saving:.1f} kg** less aluminium while maintaining process conditions.

"""

                )

            elif saving < 0:

                st.warning(

                    f"""

AI recommends **{-saving:.1f} kg** more aluminium than historical practice.

Review chemistry and process conditions before reducing aluminium.

"""

                )

            else:

                st.info(

                    "AI prediction matches the historical aluminium consumption."

                )

    # =====================================================
    # MANUAL HEAT ENTRY
    # =====================================================

    elif mode == "✍ Manual Heat Entry":

        st.markdown("""
        <h2 style="
        color:white;
        font-size:26px;
        font-weight:700;
        margin-bottom:5px;">
        📝 Manual Heat Entry
        </h2>
        """, unsafe_allow_html=True)

        st.info(
            "Enter the current LRF process parameters. Grade chemistry and oxygen will be loaded automatically."
        )

        left, right = st.columns(2)

        # =====================================================
        # LEFT PANEL
        # =====================================================

        with left:

            grade = st.selectbox(
                "Steel Grade",
                sorted(df["GRADE"].dropna().unique())
            )

            vd_nvd = st.selectbox(
                "VD / NVD",
                sorted(df["VD/NVD"].dropna().unique())
            )

            tap_weight = st.number_input(
                "Tap Weight (Ton)",
                value=105.0
            )
            oxygen = st.number_input(
               "🫧 Dissolved Oxygen (ppm)",
                min_value=0.0,
                max_value=1000.0,
               value=450.0,
               step=10.0,
               help="Measured dissolved oxygen before aluminium addition."
             )
            st.session_state["oxygen"] = oxygen
            temp = st.number_input(
                "Lifting Temperature (°C)",
                value=1600.0
            )

            opening_temp = st.number_input(
                "Opening Temperature (°C)",
                value=1585.0
            )

            al_ingot = st.number_input(
                "Al Ingot during EAF Tapping (kg)",
                value=180.0,
                step=10.0
            )

            lime = st.number_input(
                "Lime (kg)",
                value=300.0
            )

            spar = st.number_input(
                "Spar (kg)",
                value=50.0
            )

        # =====================================================
        # RIGHT PANEL
        # =====================================================

        with right:

            carbon = st.number_input(
                "Initial Carbon (%)",
                value=0.18,
                format="%.3f"
            )

            manganese = st.number_input(
                "Initial Manganese (%)",
                value=1.20,
                format="%.3f"
            )

            silicon = st.number_input(
                "Initial Silicon (%)",
                value=0.020,
                format="%.3f"
            )

            sulphur = st.number_input(
                "Initial Sulphur (%)",
                value=0.030,
                format="%.3f"
            )

            aluminium = st.number_input(
                "Initial Aluminium (%)",
                value=0.030,
                format="%.3f"
            )

            nitrogen = st.number_input(
                "Initial Nitrogen (ppm)",
                value=55.0
            )

        st.markdown("---")

        predict_btn = st.button(
            "🚀 Predict Aluminium",
            width="stretch"
        )

        if predict_btn:

            # ==========================================
            # LOAD TARGET CHEMISTRY
            # ==========================================

            target = get_grade_targets(grade)

            C_Target = target["C_Target"]
            Mn_Target = target["Mn_Target"]
            Si_Target = target["Si_Target"]
            Al_Target = target["Al_Target"]

            # ==========================================
            # LOAD GRADE OXYGEN
            # ==========================================

            Mean_Oxygen = get_grade_oxygen(grade)

            # ==========================================
            # GAP FEATURES
            # ==========================================

            Carbon_Gap = calculate_gap(carbon, C_Target)
            Mn_Gap = calculate_gap(manganese, Mn_Target)
            Si_Gap = calculate_gap(silicon, Si_Target)
            Al_Gap = calculate_gap(aluminium, Al_Target)

            # ==========================================
            # CREATE MODEL INPUT
            # ==========================================

            manual_heat = pd.DataFrame({

                "GRADE":[grade],
                "VD/NVD":[vd_nvd],

                "tap_wt_from_EAF":[tap_weight],
                 "Mean_Oxygen": [oxygen],
                "al ingot_kg__during_EAF_tapping":[al_ingot],

                "TEMP OPENING_LRF":[opening_temp],
                "LIFTING TEMP_LRF":[temp],

                "LIME_LRF":[lime],
                "SPAR":[spar],

                # "Mean_Oxygen":[Mean_Oxygen],

                "LRF_Initial_Chemistry_C":[carbon],
                "LRF_Initial_Chemistry_MN":[manganese],
                "LRF_Initial_Chemistry_S":[sulphur],
                "LRF_Initial_Chemistry_SI":[silicon],
                "LRF_Initial_Chemistry_AL":[aluminium],
                "LRF_Initial_Chemistry_N2":[nitrogen],

                "C_Target":[C_Target],
                "Mn_Target":[Mn_Target],
                "Si_Target":[Si_Target],
                "Al_Target":[Al_Target],

                "Carbon_Gap":[Carbon_Gap],
                "Mn_Gap":[Mn_Gap],
                "Si_Gap":[Si_Gap],
                "Al_Gap":[Al_Gap]

            })

            prediction = predict_heat(manual_heat)

            recommendation = generate_recommendation(prediction)

            st.session_state["prediction_done"] = True
            st.session_state["recommendation"] = recommendation
            st.session_state["predicted_al"] = recommendation["Predicted_Al"]

            st.session_state["manual_heat"] = manual_heat

            st.session_state["dashboard_data"] = {

             "selected_heat": manual_heat.iloc[0].to_dict(),

             "recommendation": {
               **manual_heat.iloc[0].to_dict(),

               "Batch Number": "MANUAL HEAT"
             },
               "recommendation": recommendation
            }  

            st.markdown("---")

            st.markdown("---")

            # =====================================================
            # KPI CARDS
            # =====================================================

            k1, k2, k3, k4 = st.columns(4)

            with k1:

                st.metric(
                    "Predicted Aluminium",
                    f"{recommendation['Predicted_Al']:.1f} kg"
                )

            # with k2:

            #     actual_al = st.number_input(
            #         "Actual Aluminium Used (kg)",
            #         min_value=0.0,
            #         value=float(recommendation["Predicted_Al"]),
            #         step=1.0,
            #         format="%.1f"
            #     )
            # saving = actual_al - recommendation["Predicted_Al"]
            with k3:

                st.metric(
                    "Confidence",
                    f"{recommendation['Confidence']} %"
                )

            # with k4:

            #    st.metric(
            #       "Potential Saving",
            #       f"{saving:.1f} kg"
            #     )
            st.markdown("---")

            # =====================================================
            # AI RECOMMENDATION
            # =====================================================

            st.subheader("🏭 AI Recommendation")

            rec_df = pd.DataFrame({

                "Material":[
                    "Al Ingot",
                    "Al Shots",
                    "Al Wire"
                ],

                "Recommended Addition":[
                    recommendation["Ingot"],
                    recommendation["Shots"],
                    recommendation["Wire"]
                ]

            })

            st.dataframe(
                rec_df,
                width="stretch",
                hide_index=True
            )

            st.markdown("---")

            # =====================================================
            # MODEL INPUT SUMMARY
            # =====================================================

            st.markdown("""
            <h2 style="
            color:white;
            font-size:24px;
            font-weight:700;">
            📋 Model Input Summary
            </h2>
            """, unsafe_allow_html=True)

            summary = pd.DataFrame({

                "Parameter":[

                    "Steel Grade",
                    "Route",
                    "Tap Weight",
                    "Opening Temperature",
                    "Lifting Temperature",
                    "Initial Aluminium",
                    "Target Aluminium",
                    "Estimated Oxygen"

                ],

                "Value":[

                    grade,
                    vd_nvd,
                    tap_weight,
                    opening_temp,
                    temp,
                    aluminium,
                    round(Al_Target,4),
                    round(Mean_Oxygen,1)

                ]

            })

            summary["Value"] = summary["Value"].astype(str)

            st.dataframe(

                summary,

                width="stretch",

                hide_index=True

            )

            st.markdown("---")

            # =====================================================
            # GAP ANALYSIS
            # =====================================================

            st.markdown("""
            <h2 style="
            color:white;
            font-size:24px;
            font-weight:700;">
            🧪 Chemistry Gap Analysis
            </h2>
            """, unsafe_allow_html=True)

            gap_df = pd.DataFrame({

                "Element":[

                    "Carbon",
                    "Manganese",
                    "Silicon",
                    "Aluminium"

                ],

                "Initial":[

                    carbon,
                    manganese,
                    silicon,
                    aluminium

                ],

                "Target":[

                    C_Target,
                    Mn_Target,
                    Si_Target,
                    Al_Target

                ],

                "Gap":[

                    Carbon_Gap,
                    Mn_Gap,
                    Si_Gap,
                    Al_Gap

                ]

            })

            st.dataframe(

                gap_df,

                width="stretch",

                hide_index=True

            )

            st.markdown("---")

            # =====================================================
            # ENGINEERING INTERPRETATION
            # =====================================================

            st.markdown("""
            <h2 style="
            color:white;
            font-size:24px;
            font-weight:700;">
            🧠 AI Engineering Interpretation
            </h2>
            """, unsafe_allow_html=True)

            st.info(f"""

### Why AI predicted **{recommendation['Predicted_Al']:.1f} kg**

The prediction is based on:

• Steel Grade (**{grade}**)

• Route (**{vd_nvd}**)

• Initial Aluminium = **{aluminium:.4f}%**

• Estimated Dissolved Oxygen = **{Mean_Oxygen:.1f} ppm**

• Grade Target Aluminium = **{Al_Target:.4f}%**

• Current Slag Practice (Lime & Spar)

• LRF Initial Chemistry

• AI model trained on historical plant heats.

""")

            st.markdown("---")

            # =====================================================
            # DOWNLOAD REPORT
            # =====================================================
            st.session_state["grade"] = grade

            st.session_state["temperature"] = temp

            st.session_state["lime"] = lime

            st.session_state["spar"] = spar

            st.session_state["carbon"] = carbon

            st.session_state["silicon"] = silicon
            report = pd.DataFrame({

                "Parameter":[

                    "Predicted Aluminium",

                    "Recovery",

                    "Confidence",

                    "Al Ingot",

                    "Al Shots",

                    "Al Wire"

                ],

                "Value":[

                    recommendation["Predicted_Al"],

                    recommendation["Recovery"],

                    recommendation["Confidence"],

                    recommendation["Ingot"],

                    recommendation["Shots"],

                    recommendation["Wire"]

                ]

            })

            csv = report.to_csv(index=False).encode("utf-8")

            st.download_button(

                "📥 Download Prediction Report",

                csv,

                file_name="AI_Aluminium_Prediction.csv",

                mime="text/csv",

                width="stretch"

            )

            st.success("✅ Prediction Completed Successfully.")

