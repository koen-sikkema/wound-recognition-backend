from databases import Database
from app.core.config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

async def get_database():
    if not database.is_connected:
        await database.connect()
    return database

async def close_database():
    if database.is_connected:
        await database.disconnect()


