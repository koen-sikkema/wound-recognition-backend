from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# BodyPart Pydantic model
class BodyPartBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class BodyPartCreate(BodyPartBase):
    pass

class BodyPartResponse(BodyPartBase):
    id: int

# WoundImage Pydantic model
class WoundImageBase(BaseModel):
    upload_date: datetime
    body_part_id: Optional[int] = None
    notes: Optional[str] = None

    class Config:
        orm_mode = True

class WoundImageCreate(WoundImageBase):
    analysis_id: Optional[int] = None

class WoundImageResponse(WoundImageBase):
    image_id: int
    body_part: Optional[BodyPartResponse] = None  # Om de body_part gegevens mee te geven

# WoundAnalysis Pydantic model
class WoundAnalysisBase(BaseModel):
    confidence: int
    size: int
    percentage_of_redness: int

    class Config:
        orm_mode = True

class WoundAnalysisCreate(WoundAnalysisBase):
    pass

class WoundAnalysisResponse(WoundAnalysisBase):
    analysis_id: int
    wound_images: List[WoundImageResponse] = []  # Relatie met WoundImage

# WoundImageMetadata Pydantic model
class WoundImageMetadataBase(BaseModel):
    device: str
    camera_software: str
    exposure_time: int
    focal_length: int
    iso: int
    gps_coordinates: Optional[str] = None

    class Config:
        orm_mode = True

class WoundImageMetadataCreate(WoundImageMetadataBase):
    image_id: int

class WoundImageMetadataResponse(WoundImageMetadataBase):
    metadata_id: int
    image_id: int
