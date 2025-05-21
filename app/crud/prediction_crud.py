from sqlalchemy.orm import Session
from app.core.database_models.prediction import Prediction
from app.utils.utils import to_dict

def save_prediction(
    db: Session,
    filename: str,
    label: str,
    confidence: float,
    wound_image: bytes,
):
    prediction = Prediction(
        filename=filename,
        label=label,
        confidence=confidence,
        woundImage=wound_image,
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction


def get_prediction(db: Session, prediction_filename: str):
    return db.query(Prediction).filter(Prediction.filename == prediction_filename).first()


def delete_prediction(db: Session, prediction_filename: str):
    prediction = db.query(Prediction).filter(Prediction.filename == prediction_filename).first()
    if prediction:
        db.delete(prediction)
        db.commit()
        return True
    return False

def delete_all_predictions(db: Session):
    db.query(Prediction).delete()
    db.commit()

def get_all_predictions(db: Session):
    predictions = db.query(Prediction).all()
    return [to_dict(pred) for pred in predictions]

def isConnected(db: Session):
    try:
        db.execute("SELECT 1")
        return True
    except Exception as e:
        print(f"Database connection error: {e}")
        return False