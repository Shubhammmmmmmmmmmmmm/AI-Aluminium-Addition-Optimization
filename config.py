# ==========================================
# PROJECT CONFIGURATION
# ==========================================

# Target Variable
TARGET = "Total_Al_LRF_kg"

# Categorical Features
CATEGORICAL_FEATURES = [
    "GRADE",
    "VD/NVD"
]

# Input Features
INPUT_FEATURES = [

    # ==========================================
    # Heat Information
    # ==========================================

    "GRADE",
    "VD/NVD",

    # ==========================================
    # Heat Size
    # ==========================================

    "tap_wt_from_EAF",

    # ==========================================
    # Aluminium during EAF tapping
    # ==========================================

    "al ingot_kg__during_EAF_tapping",

    # ==========================================
    # LRF Process
    # ==========================================

    "TEMP OPENING_LRF",
    "LIFTING TEMP_LRF",

    # ==========================================
    # Fluxes
    # ==========================================

    "LIME_LRF",
    "SPAR",

    # ==========================================
    # Grade Oxygen Master
    # ==========================================

    "Mean_Oxygen",

    # ==========================================
    # Initial Chemistry
    # ==========================================

    "LRF_Initial_Chemistry_C",
    "LRF_Initial_Chemistry_MN",
    "LRF_Initial_Chemistry_S",
    "LRF_Initial_Chemistry_SI",
    "LRF_Initial_Chemistry_AL",
    "LRF_Initial_Chemistry_N2",

    # ==========================================
    # Target Chemistry
    # ==========================================

    "C_Target",
    "Mn_Target",
    "Si_Target",
    "Al_Target",

    # ==========================================
    # Chemistry Gap
    # ==========================================

    "Carbon_Gap",
    "Mn_Gap",
    "Si_Gap",
    "Al_Gap"

]
import pandas as pd

df = pd.read_csv("clean_data/clean_dataset_ModelB.csv")

print(df[INPUT_FEATURES].isna().sum())