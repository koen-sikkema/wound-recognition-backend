from app.services.storage_service import ImageService
from app.services.model_service import ModelService
from app.core.database import SessionLocal
from sqlalchemy.orm import Session

from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_storage_service(db: Session = Depends(get_db)):
    return ImageService(db)

def get_model_service():
    return ModelService()
