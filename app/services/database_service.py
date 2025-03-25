from sqlalchemy.orm      import Session
from app.core.database   import SessionLocal
from app.core.models     import WoundImage   


class DatabaseService:
    _session = None

    @classmethod
    def get_db(cls) -> Session:
        if cls._session is None:
            cls._session = SessionLocal()
        return cls._session

    @classmethod
    def close(cls):
        if cls._session:
            cls._session.close()
            cls._session = None
    
    def save_image(self, image_data: dict):
        ''' 
        This function saves an image to the database.
        '''
        db = self.get_db()
        db_image = WoundImage(**image_data)
        db.add(db_image)
        db.commit()
        db.refresh(db_image)
        return db_image
    
