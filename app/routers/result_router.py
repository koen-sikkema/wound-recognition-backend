
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.prediction_schema import CashedPrediction
from app.services.cache_service import get_result

router = APIRouter(prefix="/results", tags=["predict"])

@router.get("/", response_model=CashedPrediction, responses={202: {"description": "Result not yet available"}})
async def get_result_route(filename: str):
    """Get the prediction result for a given filename.
    Args:
        filename (str): The name of the file for which to get the prediction result.
    Returns:
        PredictionResult: The prediction result for the given filename.
    """
    result = get_result(filename)
    if result:
        return result
    return JSONResponse(status_code=202, content={"message": "Result not yet available"})