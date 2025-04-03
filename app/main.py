from fastapi                import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File    
import os

app = FastAPI()

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

    os.makedirs("uploads", exist_ok=True)


    with open(f"uploads/{file.filename}", "wb") as buffer:
        buffer.write(await file.read())
    return {"filename": file.filename}



