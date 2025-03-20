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

@app.get("/images/{image_id}")
async def get_wound_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(WoundImage).filter(WoundImage.image_id == image_id).first()
    if image:
        return image
    return {"message": "Image not found"}
