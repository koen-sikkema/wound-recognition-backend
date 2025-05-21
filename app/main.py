
import logging
from app.core.constants         import Paths
from fastapi                    import FastAPI
from fastapi.middleware.cors    import CORSMiddleware
from app.database.database import Base, engine
from app.routers import history_router, result_router, upload_router
from app.core.ml_manager.model_manager import ModelManager


app = FastAPI()
app.include_router(history_router.router)
app.include_router(upload_router.router)
app.include_router(result_router.router)

@app.on_event("startup")
async def startup_event():
    """Load database and models during app startup."""

    logging.info("Creating database if non-existent...")
    Base.metadata.create_all(bind=engine)
    model_manager = ModelManager()
    logging.info("Loading models...")
    model_manager.initialize_model()
    
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





