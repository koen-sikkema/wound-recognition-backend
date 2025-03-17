from fastapi import FastAPI
from app.api.v1.model import router as model_router

app = FastAPI()
app.include_router(model_router, prefix="/model", tags=["Model"])


