from sqlalchemy import Column, Integer, String, LargeBinary
from database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    confidence = Column(float, unique=False)
    label = Column(String, unique=False)
    woundImage = Column(LargeBinary, unique=False)
    preproWoundImage = Column(LargeBinary, unique=False)
