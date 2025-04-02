from fastapi                import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File    
import os

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",  # Als je backend op deze poort draait
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Of gebruik ["*"] om alle origin te accepteren
    allow_credentials=True,
    allow_methods=["*"],  # Sta alle methoden toe (POST, GET, enz.)
    allow_headers=["*"],  # Sta alle headers toe
)


@app.get("/")
def read_root():
    return {"message": "Welkom bij de wondherkenningsapp!"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)


    with open(f"uploads/{file.filename}", "wb") as buffer:
        buffer.write(await file.read())
    return {"filename": file.filename}



