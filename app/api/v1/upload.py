from fastapi                        import APIRouter, Depends, UploadFile, File, Form
from app.services.upload_service    import UploadService

router = APIRouter()

@router.post("/upload")
async def upload_image(
    image: UploadFile = File(...),
    notes: str = Form(None),
    upload_service: UploadService = Depends(),
):
    result = await upload_service.process_image(image, notes)
    return {"message": "Image received successfully", "image_info": result}
