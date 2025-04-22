from fastapi                import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from fastapi import UploadFile, File    
import os
import cv2
from app.services.segment_service import segment_image
from app.services.crop_image_service import crop_image 
from app.services.preprocess_service import preprocess_image
from app.core.constants import load_model, get_prediction_labels
from app.core.model_manager import ModelManager
from app.core.constants import BEST_CNN_PATH, SAM_weights, SAM_TYPE_VIT_B
app = FastAPI()
def main():
    manager = ModelManager()
    manager.initialize_models(
        keras_model_path= BEST_CNN_PATH,
        sam_checkpoint_path=SAM_weights ,
        sam_model_type=SAM_TYPE_VIT_B
    )
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

async def upload_image(file: UploadFile = File(...)):
    """
    Upload an image to /uploads.
    """
    os.makedirs("uploads", exist_ok=True)
    try:

        # @todo 
        # seperation of concerns: save the file to a directory
        with open(f"uploads/raw_uploads/{file.filename}", "wb") as buffer:
            buffer.write(await file.read())
        filename = file.filename
        
        logging.info(f"File {file.filename} uploaded successfully")
       
        # segment the image using SAM
        image, mask, score = await segment_image(filename)
        cropped_image = crop_image(filename,image, mask)
        preprocessed_image = preprocess_image(filename, cropped_image)

        return JSONResponse(content={"message": "File uploaded successfully"}, status_code=200)
    
    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        return JSONResponse(content={"message": "Upload failed", "error": str(e)}, status_code=500)


@app.get("/predict/")
async def get_result(filename: str):
    """
    Get the result of the segmentation.
    """
    

    return {"message": "Resultaat van de segmentatie"}


