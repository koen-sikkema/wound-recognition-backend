
import logging
from app.core.model_manager import ModelManager
from app.core.store_result      import get_result
from app.core.constants         import Paths,  Config, ModelHandler
from fastapi                    import FastAPI, BackgroundTasks, UploadFile, File 
from fastapi.middleware.cors    import CORSMiddleware
from fastapi.responses          import JSONResponse
from database import Base, engine
from app.routers import prediction_router, upload_router


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(prediction_router.router)
app.include_router(upload_router.router)
app.include_router(upload_router.router)

@app.on_event("startup")
async def startup_event():
    """ Load models during app startup """
    
    logging.info("Creatin database if non-existent...")
    Base.metadata.create_all(bind=engine)
    logging.info("Loading models...")
    MODEL_MANAGER = ModelManager()
    ModelHandler.MODEL_MANAGER.initialize_model(
        keras_model_path=Paths.BEST_CNN_PATH,
    )
    logging.info("Models initialized successfully.")

logging.basicConfig(level=logging.INFO)
origins = ["*"]

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





