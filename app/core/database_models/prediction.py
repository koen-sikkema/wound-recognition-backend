from sqlalchemy import Column, Integer, String, LargeBinary, Float
from app.database.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    confidence = Column(Float, unique=False)
    label = Column(String, unique=False)
    woundImage = Column(LargeBinary, unique=False)
