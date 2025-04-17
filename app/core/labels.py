import pandas as pd

def get_prediction_labels():
    pandas_df = pd.read_csv('app/core/labels.csv')
    return pandas_df["Class"].tolist()
