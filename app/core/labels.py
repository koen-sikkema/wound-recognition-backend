import pandas as pd
from app.core.constants import (
        LABELS_CNN_PATH,
    )

def get_prediction_labels():
    pandas_df = pd.read_csv(LABELS_CNN_PATH)
    return pandas_df["Class"].tolist()
