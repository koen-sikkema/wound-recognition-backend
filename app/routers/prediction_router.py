from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from typing import List

from app.services.database_service.prediction_service import (
    get_all_predictions,
    delete_all_predictions,
)

router = APIRouter(prefix="/predictions", tags=["get_predictions"])

@router.get("/")
def read_all_predictions(db: Session = Depends(get_db)):
    return get_all_predictions(db)

@router.delete("/")
def delete_all_predictions_route(db: Session = Depends(get_db)):
    delete_all_predictions(db)
    return {"message": "All predictions deleted successfully."}

