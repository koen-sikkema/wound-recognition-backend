
from pathlib                                import Path
import pandas as pd

def get_prediction_labels():
    """
    Reads the labels from the CSV file and returns them as a list.
    """
    if not Paths.LABELS_CSV_NL.exists():
        raise FileNotFoundError(f"Labels CSV not found at {Paths.LABELS_CSV_NL}")
    pandas_df = pd.read_csv(Paths.LABELS_CSV_NL)
    return pandas_df["Class"].tolist()



class Paths:
    """
    A class to hold paths used in the application.
    """
    BASE_DIR = Path(__file__).resolve().parent.parent
    MODEL_DIR = BASE_DIR / "ml_assets"
    BEST_CNN_PATH = MODEL_DIR / "best_cnn.h5"
    LABELS_CSV_ENG = MODEL_DIR / "labels_cnn.csv"
    LABELS_CSV_NL = MODEL_DIR / "labels_cnn_nl.csv"


class Config:
    """
    A class to hold configuration constants.
    """
    PREPROCESS_SIZE = (128, 128)
    
    _labels = None

    @classmethod
    def get_labels(cls):
        if cls._labels is None:
            cls._labels = get_prediction_labels()
        return cls._labels

 








    

