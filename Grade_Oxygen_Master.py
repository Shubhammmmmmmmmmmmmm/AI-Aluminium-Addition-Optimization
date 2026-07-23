import pandas as pd

# ==========================================
# LOAD ORIGINAL MASTER DATA
# ==========================================

df = pd.read_excel(
    "data/2ndTime_MASTER_DATASET_FINAL_v2 (4).xlsx"
)

# ==========================================
# KEEP ONLY REQUIRED COLUMNS
# ==========================================

df = df[[
    "GRADE",
    "dissolved_O2(ppm)during_tapping_from_EAF"
]]

# Remove blank oxygen values
# ==========================================
# CONVERT OXYGEN TO NUMERIC
# ==========================================

df["dissolved_O2(ppm)during_tapping_from_EAF"] = pd.to_numeric(
    df["dissolved_O2(ppm)during_tapping_from_EAF"],
    errors="coerce"      # converts "---", "NA", etc. to NaN
)

# Remove missing oxygen values
df = df.dropna(
    subset=["dissolved_O2(ppm)during_tapping_from_EAF"]
)

# Clean grade names
df["GRADE"] = (
    df["GRADE"]
    .astype(str)
    .str.upper()
    .str.strip()
)

# ==========================================
# CREATE GRADE OXYGEN MASTER
# ==========================================

oxygen_master = (
    df.groupby("GRADE")[
        "dissolved_O2(ppm)during_tapping_from_EAF"
    ]
    .agg(
        Mean_Oxygen="mean",
        Median_Oxygen="median",
        Min_Oxygen="min",
        Max_Oxygen="max",
        Std_Oxygen="std",
        Samples="count"
    )
    .reset_index()
)

oxygen_master.to_excel(
    "Grade_Oxygen_Master.xlsx",
    index=False
)
print(df["dissolved_O2(ppm)during_tapping_from_EAF"].describe())
print(oxygen_master.head(20))

print("\nTotal Grades :", len(oxygen_master))