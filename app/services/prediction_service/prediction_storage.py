from app.crud.prediction_crud import save_prediction as crud_save
from sqlalchemy.orm import Session

def store_prediction_to_db(
    db: Session,
    filename: str,
    label: str,
    confidence: float,
    image_bytes: bytes,
):
    """safe prediction to database."""
    crud_save(db, filename, label, confidence, image_bytes)
