from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from typing import List

from app.services.database_dervice.prediction_service import (
    get_all_predictions,
    delete_all_predictions,
)
router = APIRouter()

router = APIRouter(prefix="/get_all_predictions", tags=["get_predictions"])
router = APIRouter(prefix="/delete_all_predictions", tags=["delete_predictions"])


@router.get("/get_all_predictions/")
def read_all_predictions(db: Session = Depends(get_db)):
    return get_all_predictions(db)

@router.get("/delete_all_predictions/")
def delete_all_predictions_route(db: Session = Depends(get_db)):
    delete_all_predictions(db)
    return {"message": "All predictions deleted successfully."}

