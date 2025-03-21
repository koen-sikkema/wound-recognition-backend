from sqlalchemy.orm     import Session
from fastapi            import FastAPI, Depends
from sqlalchemy.orm     import Session
from core.database      import get_database, close_database
from core.models        import WoundImage

app = FastAPI()


@app.get("/images/{image_id}")
async def get_wound_image(image_id: int, db: Session = Depends(get_database)):
    '''
        This function returns the wound image with the given image_id.'
    '''
    image = db.query(WoundImage).filter(WoundImage.image_id == image_id).first()
    if image:
        return image
    Depends(close_database)
    return {"message": "Image not found"}
