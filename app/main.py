
import logging
from app.core.constants         import Paths
from fastapi                    import FastAPI
from fastapi.middleware.cors    import CORSMiddleware
from app.database.database import Base, engine
from app.routers import history_router, result_router, upload_router
from app.core.ml_manager.model_manager import ModelManager
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown logic."""
    logging.info("Creating database if non-existent...")
    Base.metadata.create_all(bind=engine)

    logging.info("Loading models...")
    model_manager = ModelManager()
    model_manager.initialize_model()
    logging.info("Models initialized successfully.")

    yield  

    logging.info("Shutting down...")


app = FastAPI(lifespan=lifespan, title="Wondherkenningsapp API", description="API voor wondherkenning met machine learning", version="1.0.0")
app.include_router(history_router.router)
app.include_router(upload_router.router)
app.include_router(result_router.router)


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





