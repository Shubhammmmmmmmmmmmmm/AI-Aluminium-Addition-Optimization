import pandas as pd

# # =====================================================
# # LOAD DATASET
# # =====================================================

def load_dataset():

    df = pd.read_csv("clean_data/clean_dataset.csv")

    return df


