from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from typing import List
from app.schemas.prediction_schema import AllPredictionsResponse

from app.crud.prediction_crud import (
    get_all_predictions,
    delete_all_predictions,
)

router = APIRouter(prefix="/predictions", tags=["Prediction history"])

@router.get("/", response_model=AllPredictionsResponse)
def read_all_predictions(db: Session = Depends(get_db)):
    """
    Get all predictions from the database.
    """
    predictions = get_all_predictions(db)
    return {"predictions": predictions} 

@router.delete("/")
def delete_all_predictions_route(db: Session = Depends(get_db)):
    """
    Delete all predictions from the database.
    """
    delete_all_predictions(db)
    return {"message": "All predictions deleted successfully."}

