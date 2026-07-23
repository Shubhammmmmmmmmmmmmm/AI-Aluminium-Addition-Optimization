import joblib
import pandas as pd

# ============================================
# LOAD MODEL
# ============================================

model = joblib.load("models/extra_trees.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")


# ============================================
# PREDICTION FUNCTION
# ============================================

def predict_heat(heat_df):

    # Always ensure DataFrame
    if isinstance(heat_df, pd.Series):
        heat_df = heat_df.to_frame().T

    X = heat_df.copy()

    # Remove target
    if "Total_Al_LRF_kg" in X.columns:
        X = X.drop(columns=["Total_Al_LRF_kg"])

    # One-hot encode
    X = pd.get_dummies(X)

    # Match training columns
    X = X.reindex(columns=feature_columns, fill_value=0)
    #####
    # print("="*60)
    # print("INPUT COLUMNS")
    # print("="*60)
    # print(X.columns.tolist())p
    ####
    prediction = model.predict(X)
    prediction = prediction*0.90
    return prediction[0]