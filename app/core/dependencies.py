from app.database.database import SessionLocal
from sqlalchemy.orm import Session

def get_db() -> Session:
    """
    Dependency that provides a database session for FastAPI routes.
    Yields a session object and ensures it is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
