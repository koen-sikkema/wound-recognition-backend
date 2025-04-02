from fastapi                import FastAPI
from app.api.v1             import ML       
from app.api.v1             import upload     
from sqlalchemy.orm         import Session
from app.core.dependencies  import get_db
from app.core.database      import engine, SessionLocal 

# initialize the FastAPI app
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welkom bij de wondherkenningsapp!"}


# Add the routers to the app
app.include_router(upload.router,  tags=["upload"])


