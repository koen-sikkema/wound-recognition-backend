from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.services.image_service.upload_handler import handle_upload

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/")
async def upload_image(background_tasks: BackgroundTasks, file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Upload an image file and process it in the background.
    """
    try:
        result = handle_upload(background_tasks, file, db)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
