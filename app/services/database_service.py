from sqlalchemy.orm     import Session
from core.database      import SessionLocal

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
