from sqlalchemy.orm import Session

class StorageService:
    def __init__(self, db: Session):
        self.db = db

