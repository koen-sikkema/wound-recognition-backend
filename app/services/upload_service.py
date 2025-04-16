from fastapi import FastAPI, UploadFile, File    
from pydantic import BaseModel


class Upload(BaseModel):
    file: UploadFile = File(...)
    

