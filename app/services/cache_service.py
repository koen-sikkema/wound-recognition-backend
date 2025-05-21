
from typing import Optional, Dict
from app.schemas.prediction_schema import CashedPrediction


results: Dict[str, CashedPrediction] = {}

def store_result(filename: str, label: str, score: float):
    """function stores result for pickup from frontend"""
    
    results[filename] = CashedPrediction(
        filename = filename,
        label = label,
        confidence = score,
    )


def get_result(filename: str) -> Optional[CashedPrediction]:
    """
    getter for predictionresult
    """
    return results.get(filename)