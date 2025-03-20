from fastapi                import FastAPI
from app.api.v1             import model       
from app.api.v1             import upload     
from sqlalchemy.orm         import Session

from app.core.models        import Base, BodyPart
from app.core.database      import engine, SessionLocal 

# initialize the FastAPI app
app = FastAPI()

def init_db():
    '''
        This function initializes the database.
    '''
    Base.metadata.create_all(bind=engine)

def create_initial_body_parts(db: Session):
    '''
        This function fills the BodyPart table with initial values.
    '''
    body_parts = [
        "Right leg",
        "Left leg",
        "Right arm",
        "Left arm",
        "Torso",
        "Head",
        "Back",
        "Hand",
        "Foot"
    ]
    for part in body_parts:
        if not db.query(BodyPart).filter(BodyPart.name == part).first():
            db.add(BodyPart(name=part))
    
    db.commit()


@app.on_event("startup")
async def startup():
    '''
        This function is called when the application starts.
    '''
    print("Starting up...")
    print("Initializing database...")
    init_db()
    print("Database initialized.")
    db = SessionLocal()
    print("filling BodyPart table with initial values...")
    create_initial_body_parts(db)
    print("BodyPart table filled.")
    print("closing database connection...")
    db.close()
    print("Startup complete.")


@app.get("/")
def read_root():
    return {"message": "Welkom bij de wondherkenningsapp!"}


# Add the routers to the app
app.include_router(upload.router,  tags=["upload"])


