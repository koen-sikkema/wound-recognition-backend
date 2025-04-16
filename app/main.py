from fastapi                import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from fastapi import UploadFile, File    
import os
from segment_anything import SamPredictor, sam_model_registry
import cv2

from app.services.upload_service import Upload 

app = FastAPI()
sam = sam_model_registry["vit_b"](checkpoint=r"SAM_weights\sam_vit_b_01ec64.pth")

# sam = sam_model_registry["vit_b"](checkpoint="app/SAM_weights/sam_vit_b_01ec64.pth")
predictor = SamPredictor(sam)

logging.basicConfig(level=logging.INFO)
origins = [
    "http://localhost",
    "http://localhost:8000",  
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.get("/")
def read_root():
    return {"message": "Welkom bij de wondherkenningsapp!"}
    
@app.post("/upload/")

async def upload_image(file: Upload):
    """
    Upload an image to /uploads.
    """
    os.makedirs("uploads", exist_ok=True)
    try:
        # @todo 
        # seperation of concerns: save the file to a directory
        with open(f"uploads/raw_uploads/{file.filename}", "wb") as buffer:
            buffer.write(await file.read())
        
        logging.info(f"File {file.filename} uploaded successfully")

        return JSONResponse(content={"message": "File uploaded successfully"}, status_code=200)
    
    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        return JSONResponse(content={"message": "Upload failed", "error": str(e)}, status_code=500)





