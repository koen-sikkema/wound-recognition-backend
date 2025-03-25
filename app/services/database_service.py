from sqlalchemy.orm import Session
from app.core.database import SessionLocal, get_database, close_database
from app.core.models import WoundImage

class DatabaseService:

    async def save_image(self, image_data: dict):
        ''' 
        This function saves an image to the database.
        '''
        await get_database()  # Open de databaseverbinding
        db = SessionLocal()
        try:
            db_image = WoundImage(**image_data)
            db.add(db_image)
            db.commit()
            db.refresh(db_image)
            return db_image
        finally:
            db.close()  # Sluit de sessie
            await close_database()  # Sluit de databaseverbinding

