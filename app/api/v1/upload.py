from fastapi                                import APIRouter, Depends, UploadFile, File, Form
from app.services.upload_service            import UploadService 


router = APIRouter()

@router.post("/upload")
async def upload_image(
    image: UploadFile = File(...),
    notes: str = Form(None),
    upload_service: UploadService = Depends()
):
    ''' 
        This function uploads an image and returns some information about it.
    '''
    return await upload_service.process_image(image, notes=notes)   


