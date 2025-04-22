# from app.core.database                      import SessionLocal
from sqlalchemy.orm                         import Session
from pathlib                                import Path
from fastapi                                import Depends
from app.core.labels                        import get_prediction_labels
from tensorflow.keras.models                import load_model
import pandas as pd

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
class Config:
    """
    A class to hold constants used in the application.
    """
    PREPROCESS_SIZE = (128, 128)
    LABELS = get_prediction_labels()
    SAM_WEIGHTS = r'C:\Users\koens\Documents\GitHub\wound-recognition-backend\SAM_weights/sam_vit_b_01ec64.pth' 
    SAM_TYPE_VIT_B = "vit_b"

class Paths:
    """
    A class to hold paths used in the application.
    """
    BASE_DIR = Path(__file__).resolve().parent.parent
    UPLOADS_DIR = BASE_DIR / "uploads"
    MODEL_DIR = BASE_DIR / "ml-model"
    SAM_WEIGHTS = MODEL_DIR / "sam_vit_b_01ec64.pth"
    BEST_CNN_PATH = MODEL_DIR / "best_cnn.h5"
    LABELS_CSV = MODEL_DIR / "labels_cnn.csv"
    UPLOADS_MASKED = UPLOADS_DIR / "masked"
    UPLOADS_RAW = UPLOADS_DIR / "raw"
    UPLOADS_PREPROCESSED = UPLOADS_DIR / "preprocessed"






    

