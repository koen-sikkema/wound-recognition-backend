
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.prediction_schema import CachedPrediction
from app.services.prediction_service.cache_handler import get_cached_prediction

router = APIRouter(prefix="/results", tags=["predict"])

@router.get("/", response_model=CachedPrediction, responses={202: {"description": "Result not yet available"}})
async def get_result_route(filename: str):
    """Get the prediction result for a given filename.
    Args:
        filename (str): The name of the file for which to get the prediction result.
    Returns:
        PredictionResult: The prediction result for the given filename.
    """
    result = get_cached_prediction(filename)
    if result:
        return result
    
    return JSONResponse(status_code=202, content={"message": "Result not yet available"})