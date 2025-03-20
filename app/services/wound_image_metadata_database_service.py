from sqlalchemy.orm     import Session
from fastapi            import FastAPI, Depends
from sqlalchemy.orm     import Session
from core.database      import get_database
from core.models        import WoundImage

app = FastAPI()

# Dependency voor de database
def get_db():
    db = get_database()
    try:
        yield db
    finally:
        db.close()

@app.get("/metadata/{metadata_id}")
async def get_wound_image_metadata(metadata_id: int, db: Session = Depends(get_db)):
    metadata = db.query(WoundImage).filter(WoundImage.metadata_id == metadata_id).first()
    if metadata:
        return metadata
    return {"message": "Metadata not found"}