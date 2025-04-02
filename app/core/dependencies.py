from app.services.upload_service            import UploadService   

from app.core.database                      import SessionLocal
from sqlalchemy.orm                         import Session

from fastapi                                import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_upload_service():
    return UploadService()

    

