
from sqlalchemy.orm                         import Session
from pathlib                                import Path
from fastapi                                import Depends
from tensorflow.keras.models                import load_model
import pandas as pd

def get_prediction_labels():
    pandas_df = pd.read_csv(Paths.LABELS_CSV_NL)
    return pandas_df["Class"].tolist()


class Paths:
    """
    A class to hold paths used in the application.
    """
    BASE_DIR = Path(__file__).resolve().parent.parent
    UPLOADS_DIR = BASE_DIR / "uploads"
    MODEL_DIR = BASE_DIR / "ml-model"
    BEST_CNN_PATH = MODEL_DIR / "best_cnn.h5"
    LABELS_CSV_ENG = MODEL_DIR / "labels_cnn.csv"
    LABELS_CSV_NL = MODEL_DIR / "labels_cnn_nl.csv"
    UPLOADS_MASKED = UPLOADS_DIR / "masked"
    UPLOADS_RAW = UPLOADS_DIR / "raw"
    UPLOADS_PREPROCESSED = UPLOADS_DIR / "preprocessed"


class Config:
    """
    A class to hold constants used in the application.
    """
    PREPROCESS_SIZE = (128, 128)
    LABELS = get_prediction_labels()
    SAM_TYPE_VIT_B = "vit_b"
 

class ModelHandler:
    '''
    seperate class for model manager
    '''
    
    from app.core.model_manager                 import ModelManager
    MODEL_MANAGER = ModelManager()







    

