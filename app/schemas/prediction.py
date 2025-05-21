from pydantic import BaseModel 
from typing import List
from typing import Optional

class PredictionCreate(BaseModel):
    filename: str
    label: str
    confidence: float
    woundImage: bytes


class PredictionRead(PredictionCreate):
    id: int
    class Config:
        orm_mode = True

class PredictionStorageResponse(BaseModel):
    id: int
    filename: str
    label: str
    confidence: float
    woundImage: bytes

class AllPredictionsResponse(BaseModel):
    predictions: List[PredictionStorageResponse]
