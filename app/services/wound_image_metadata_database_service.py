from sqlalchemy.orm     import Session
from fastapi            import FastAPI, Depends
from sqlalchemy.orm     import Session
from core.database      import get_database, close_database
from core.models        import WoundImage

app = FastAPI()


@app.get("/metadata/{metadata_id}")
async def get_wound_image_metadata(metadata_id: int, db: Session = Depends(get_database)):
    metadata = db.query(WoundImage).filter(WoundImage.metadata_id == metadata_id).first()
    if metadata:
        return metadata
    Depends(close_database)
    return {"message": "Metadata not found"}