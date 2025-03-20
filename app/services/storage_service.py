from sqlalchemy.orm     import Session

class StorageService:
    def __init__(self, db: Session):
        self.db = db
    
    def store_image(self, image_data: bytes, notes: str = None):        
        ''' 
            This function stores an image in the database.
        '''
        pass    