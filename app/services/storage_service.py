from sqlalchemy.orm import Session
from app.models.image import Image

class Storage_service:
    def __init__(self, db: Session):
        self.db = db

    def save_image(self, filename: str, data: bytes, notes: str = None):
        '''
        This function saves an image to the database.
        '''
        db_image = Image(filename=filename, data=data, notes=notes)
        self.db.add(db_image)
        self.db.commit()
        self.db.refresh(db_image)
        return db_image
