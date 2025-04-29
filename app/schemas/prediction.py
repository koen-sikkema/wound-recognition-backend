from pydantic import BaseModel

class PredictionResult(BaseModel):
    filename: str
    label: str
    confidence: float
