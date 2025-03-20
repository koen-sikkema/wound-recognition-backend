from fastapi import APIRouter, Depends
from app.services.storage_service import StorageService

router = APIRouter()

@router.get("/storage")
async def get_storage_info(storage_service: StorageService = Depends()):
    return storage_service.get_storage_info()