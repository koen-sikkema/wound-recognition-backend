from pydantic import BaseModel
from typing import List
from typing import Optional

class PredictionCreate(BaseModel):
    filename: str
    label: str
    confidence: float
    woundImage: bytes
    preproWoundImage: bytes 

class PredictionRead(PredictionCreate):
    id: int
    class Config:
        orm_mode = True

class PredictionStorageResponse(BaseModel):
    id: int
    filename: str
    label: str
    confidence: float
    woundImage: Optional[str]
    preproWoundImage: Optional[str]

class AllPredictionsResponse(BaseModel):
    predictions: List[PredictionStorageResponse]
