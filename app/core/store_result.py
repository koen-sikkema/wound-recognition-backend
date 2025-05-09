
from typing import Optional, Dict
from app.schemas.prediction import PredictionResult


results: Dict[str, PredictionResult] = {}

def store_result(filename: str, label: str, score: float):
    results[filename] = {
        "filename": filename,
        "label": label,
        "confidence" : score
    }


def get_result(filename: str) -> Optional[PredictionResult]:
    return results.get(filename)