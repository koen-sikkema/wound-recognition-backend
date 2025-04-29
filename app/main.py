
import logging
import os
import cv2
from app.services.image_result_service import process_image_to_result
from app.core.model_manager import ModelManager
from app.core.store_result      import get_result
from app.core.constants         import Paths,  Config, ModelHandler
from fastapi                    import FastAPI, BackgroundTasks, UploadFile, File 
from fastapi.middleware.cors    import CORSMiddleware
from fastapi.responses          import JSONResponse


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """ Load models during app startup """

    MODEL_MANAGER = ModelManager()
    ModelHandler.MODEL_MANAGER.initialize_model(
        keras_model_path=Paths.BEST_CNN_PATH,
        sam_checkpoint_path=Paths.SAM_WEIGHTS,
        sam_model_type=Config.SAM_TYPE_VIT_B
    )
    logging.info("Models initialized successfully.")


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
async def upload_image(background_tasks: BackgroundTasks, file: UploadFile = File(...), ):
    """
    Upload a file, process it in the background, and return a response immediately.
    """
    os.makedirs(Paths.UPLOADS_RAW, exist_ok=True)

    try:
        # Sla het bestand op
        with open(f"{Paths.UPLOADS_RAW}/{file.filename}", "wb") as buffer:
            buffer.write(await file.read())
        
        logging.info(f"File {file.filename} uploaded successfully")

        background_tasks.add_task(process_image_to_result, file.filename)
        
        # give status code 200 to indicate success
        return JSONResponse(content={"message": "File uploaded successfully, processing in background"}, status_code=200)
    
    except Exception as e:
        logging.error(f"Error uploading file: {e}", exc_info=True)
        return JSONResponse(content={"message": "Upload failed", "error": str(e)}, status_code=500)

@app.get("/predict/")
async def get_result_route(filename: str):
    result = get_result(filename)
    if result:
        return {
            "filename": filename,
            "label": result["label"],
            "confidence": result["score"]
        }
    return JSONResponse(status_code=202, content={"message": "Resultaat nog niet beschikbaar"})



