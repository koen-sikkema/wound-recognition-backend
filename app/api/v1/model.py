from fastapi                        import APIRouter, Depends, UploadFile, File, Form
from app.services.model_service     import ModelService
from app.services.storage_service   import StorageService

router = APIRouter()

@router.post("/predict")
async def predict():
    return {"prediction": "some prediction"}
