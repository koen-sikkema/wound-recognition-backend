import pandas as pd

def get_prediction_labels():
    pandas_df = pd.read_csv(r'app/ml-model/labels_cnn.csv')
    return pandas_df["Class"].tolist()
