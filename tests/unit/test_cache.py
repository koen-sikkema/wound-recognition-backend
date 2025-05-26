import pytest
import pandas as pd
from unittest.mock import patch, MagicMock

def test_cache_prediction():
    """Test caching of prediction results."""
    from app.services.prediction_service.cache_handler import cache_prediction, get_cached_prediction
    from app.schemas.prediction_schema import CachedPrediction

    filename = "test_image.jpg"
    label = "cat"
    score = 0.95

    cache_prediction(filename, label, score)
    
    cached_result = get_cached_prediction(filename)
    
    assert cached_result == CachedPrediction(
        filename=filename,
        label=label,
        confidence=score
    ), "Cached prediction should match the input values"

def test_get_cached_prediction_not_found():
    """Test getting a cached prediction that does not exist."""
    from app.services.prediction_service.cache_handler import get_cached_prediction

    filename = "non_existent_image.jpg"
    
    cached_result = get_cached_prediction(filename)
    
    assert cached_result is None, "Should return None for non-existent cached prediction"