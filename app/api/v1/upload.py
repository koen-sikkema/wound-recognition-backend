from fastapi                                import APIRouter, Depends, UploadFile, File, Form
from app.services.upload_service            import UploadService 
from app.services.database_service          import DatabaseService  

router = APIRouter()

@router.post("/upload")
async def upload_image(
    save_to_database: bool = Form(None),
    image: UploadFile = File(...),
    bodypart: str = Form(None), 
    notes: str = Form(None),
    upload_service: UploadService = Depends(),
    storage_service: DatabaseService = Depends()    
    
):
    result = await upload_service.process_image(image, bodypart=bodypart, notes=notes)

    if result is None:
        return {"message": "Image could not be processed"}
    
    if save_to_database is not None:             
        if save_to_database:
            await storage_service.save_image(result)  
        return {"message": "image will be saved in database", "image_info": result}
    return {"message": "Image received successfully", "image_info": result}
