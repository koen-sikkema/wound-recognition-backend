
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.prediction_result import PredictionResult
from app.core.store_result import get_result

router = APIRouter()
router = APIRouter(prefix="/predict", tags=["predict"])

@router.get("/predict/", response_model=PredictionResult, responses={202: {"description": "Result not yet available"}})
async def get_result_route(filename: str):
    result = get_result(filename)
    if result:
        return result
    return JSONResponse(status_code=202, content={"message": "Result not yet available"})