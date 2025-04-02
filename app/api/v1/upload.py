from fastapi                                import APIRouter, Depends, UploadFile, File, Form
from app.services.upload_service            import UploadService 


router = APIRouter()

@router.post("/upload")

async def upload_image(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        buffer.write(await file.read())
    return {"filename": file.filename}
