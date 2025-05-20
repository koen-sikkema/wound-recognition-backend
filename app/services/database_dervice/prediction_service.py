from sqlalchemy.orm import Session
from models.prediction import Prediction
from schemas.prediction import PredictionCreate
from base64 import b64encode


def create_prediction(db: Session, prediction_data: PredictionCreate):
    prediction = Prediction(**prediction_data.dict())
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction

def save_prediction(db, filename, label, confidence, wound_image, prepro_image):
    prediction = Prediction(
        filename=filename,
        label=label,
        confidence=confidence,
        woundImage=wound_image,
        preproWoundImage=prepro_image
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

    def to_dict(p):
        return {
            "id": p.id,
            "filename": p.filename,
            "label": p.label,
            "confidence": p.confidence,
            "woundImage": b64encode(p.woundImage).decode("utf-8") if p.woundImage else None,
            "preproWoundImage": b64encode(p.preproWoundImage).decode("utf-8") if p.preproWoundImage else None,
        }

    return [to_dict(pred) for pred in predictions]

def isConnected(db: Session):
    try:
        db.execute("SELECT 1")
        return True
    except Exception as e:
        print(f"Database connection error: {e}")
        return False