from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException
from app.services.upload_service import handle_upload

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/upload/")
async def upload_image(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    try:
        result = handle_upload(background_tasks, file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
