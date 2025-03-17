from fastapi import APIRouter, Depends, UploadFile, File, Form
from app.services.model_service import ModelService
from app.services.storage_service import StorageService

router = APIRouter()

@router.post("/predict")
async def predict(
    image: UploadFile = File(...),
    save_image: bool = Form(...),
    notes: str = Form(None),
    model_service: ModelService = Depends(),
    storage_service: StorageService = Depends()
):
    image_data = await image.read()
    prediction = model_service.predict(image_data)

    saved_image = None
    if save_image:
        saved_image = storage_service.save_image(image.filename, image_data, notes)

    return {
        "prediction": prediction,
        "saved_image_id": saved_image.id if saved_image else None
    }
