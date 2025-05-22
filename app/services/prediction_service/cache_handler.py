
from typing import Optional, Dict
from app.schemas.prediction_schema import CachedPrediction


results: Dict[str, CachedPrediction] = {}

def cache_prediction(filename: str, label: str, score: float):
    """
    Cache the prediction result for a given filename.
    Args:
        filename (str): The name of the file for which to get the prediction result.
        label (str): The predicted label.
        score (float): The confidence score of the prediction.
    """
    results[filename] = CachedPrediction(
        filename = filename,
        label = label,
        confidence = score,
    )


def get_cached_prediction(filename: str) -> Optional[CachedPrediction]:
    """
    getter for predictionresult on filename
    """
    return results.get(filename)