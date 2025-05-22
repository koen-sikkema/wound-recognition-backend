
from typing import Optional, Dict
from app.schemas.prediction_schema import CachedPrediction


results: Dict[str, CachedPrediction] = {}

def store_result(filename: str, label: str, score: float):
    """function stores result for pickup from frontend"""
    
    results[filename] = CachedPrediction(
        filename = filename,
        label = label,
        confidence = score,
    )


def get_result(filename: str) -> Optional[CachedPrediction]:
    """
    getter for predictionresult
    """
    return results.get(filename)