from fastapi                        import APIRouter, Depends, UploadFile, File, Form
from app.services.ML_service     import MLService
from app.services.storage_service   import StorageService

router = APIRouter()

@router.post("/predict")
async def predict():
    return {"prediction": "some prediction"}
