
from sqlalchemy                 import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm             import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BodyPart(Base):
    __tablename__ = "body_parts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"<BodyPart(id={self.id}, name={self.name})>"


class WoundImage(Base):
    __tablename__ = "wound_images"
    
    image_id = Column(Integer, primary_key=True, index=True)
    analysis_id = Column(Integer, ForeignKey("wound_analyses.analysis_id"), nullable=True)
    upload_date = Column(DateTime, nullable=False)
    body_part_id = Column(Integer, ForeignKey("body_parts.id"), nullable=True)
    notes = Column(String(255), nullable=True)

    analysis = relationship("WoundAnalysis", back_populates="wound_images")
    body_part = relationship("BodyPart", back_populates="wound_images")

    def __repr__(self):
        return f"<WoundImage(image_id={self.image_id}, upload_date={self.upload_date}, body_part={self.body_part_id}, notes={self.notes})>"


class WoundAnalysis(Base):
    __tablename__ = "wound_analyses"
    
    analysis_id = Column(Integer, primary_key=True, index=True)
    confidence = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    percentage_of_redness = Column(Integer, nullable=False)
    
    wound_images = relationship("WoundImage", back_populates="analysis")

    def __repr__(self):
        return f"<WoundAnalysis(analysis_id={self.analysis_id}, confidence={self.confidence}, size={self.size}, percentage_of_redness={self.percentage_of_redness})>"

class WoundImageMetadata(Base):
    __tablename__ = "wound_image_metadata"
    
    metadata_id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey("wound_images.image_id"), nullable=False)
    device = Column(String(255), nullable=False)
    camera_software = Column(String(255), nullable=False)
    exposure_time = Column(Integer, nullable=False)
    focal_length = Column(Integer, nullable=False)
    iso = Column(Integer, nullable=False)
    gps_coordinates = Column(String(255), nullable=True)

    wound_image = relationship("WoundImage", backref="metadata")

    def __repr__(self):
        return f"<WoundImageMetadata(metadata_id={self.metadata_id}, image_id={self.image_id}, device={self.device}, camera_software={self.camera_software})>"

BodyPart.wound_images = relationship("WoundImage", back_populates="body_part")
