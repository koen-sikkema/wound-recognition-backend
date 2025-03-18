from fastapi            import FastAPI
from app.api.v1         import model       
from app.api.v1         import upload      

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}   

app.include_router(upload.router,  tags=["upload"])

app.include_router(model.router, tags=["model"])