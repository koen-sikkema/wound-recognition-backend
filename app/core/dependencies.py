from app.core.database                      import SessionLocal
from sqlalchemy.orm                         import Session
from pathlib                                import Path
from fastapi                                import Depends
from app.core.labels                        import get_prediction_labels
from tensorflow.keras.models                import load_model

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

MODEL_PATH = Path("ml-model/best_cnn.h5")
CLASSES = get_prediction_labels()

def load_model():
    model = load_model(MODEL_PATH)
    print("CNN model loaded successfully")
    return model



    

