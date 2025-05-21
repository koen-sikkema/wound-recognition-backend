
import logging
from app.core.model.model_handler     import ModelHandler
from app.core.constants         import Paths
from fastapi                    import FastAPI
from fastapi.middleware.cors    import CORSMiddleware
from app.services.database_service.database import Base, engine
from app.routers import prediction_router, upload_router, predict_router

app = FastAPI()
app.include_router(prediction_router.router)
app.include_router(upload_router.router)
app.include_router(predict_router.router)

@app.on_event("startup")
async def startup_event():
    """Load database and models during app startup."""
    logging.info("Creating database if non-existent...")
    Base.metadata.create_all(bind=engine)
    
    logging.info("Loading models...")
    ModelHandler.MODEL_MANAGER.initialize_model()
    
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





