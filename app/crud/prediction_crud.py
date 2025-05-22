from sqlalchemy.orm import Session
from app.core.database_models.prediction import Prediction
from app.utils.encoding import to_dict
import logging

def save_prediction(
    
    db: Session,
    filename: str,
    label: str,
    confidence: float,
    wound_image: bytes,
) -> Prediction:
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


def get_prediction(db: Session, prediction_filename: str) -> Prediction:
    """
    Get a prediction by filename.
    """
    return db.query(Prediction).filter(Prediction.filename == prediction_filename).first()


def delete_prediction(db: Session, prediction_filename: str) -> bool:
    """
    Delete a prediction by filename.
    Returns True if the prediction was deleted, False if it was not found.
    """
    prediction = db.query(Prediction).filter(Prediction.filename == prediction_filename).first()
    if prediction:
        db.delete(prediction)
        db.commit()
        return True
    return False

def delete_all_predictions(db: Session) -> None:
    """
    Delete all predictions from the database.
    """
    db.query(Prediction).delete()
    db.commit()

def get_all_predictions(db: Session) -> list [dict]:
    """
    Get all predictions from the database.
    Returns a list of dictionaries representing the predictions.
    """
    predictions = db.query(Prediction).all()
    return [to_dict(pred) for pred in predictions]

def isConnected(db: Session):
    try:
        db.execute("SELECT 1")
        return True
    except Exception as e:
        logging.error(f"Database connection error: {e}")
        return False