
from typing import Optional, Dict
from app.schemas.prediction import PredictionResult


results: Dict[str, PredictionResult] = {}

def store_result(filename: str, label: str, score: float):
    """function stores result for pickup from frontend"""
    
    results[filename] = {
        "filename": filename,
        "label": label,
        "confidence" : score
    }


def get_result(filename: str) -> Optional[PredictionResult]:
    """
    getter for predictionresult
    """
    return results.get(filename)