import pytest
import os
import tempfile
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app  
from app.core.dependencies import get_db
from app.database.database import Base
from io import BytesIO
from PIL import Image
import numpy as np
from app.core.constants import Config

@pytest.fixture
def dummy_image_bytes():
    """
    Returns a PNG image (128x128 RGB) as bytes,
    suitable for use in the pipeline.
    """
    size = Config.PREPROCESS_SIZE  
    image = Image.fromarray((np.random.rand(*size, 3) * 255).astype(np.uint8))
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()

@pytest.fixture(scope="function")
def test_db():
    # Maak tijdelijk bestand aan
    tmp_file = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp_file.close()  # Sluit zodat SQLite kan openen

    test_db_url = f"sqlite:///{tmp_file.name}"
    engine = create_engine(test_db_url, connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Drop tables voor netheid (optioneel)
        Base.metadata.drop_all(bind=engine)
        engine.dispose()  # Sluit alle connecties en resources

        # Verwijder het bestand nadat engine gesloten is
        os.unlink(tmp_file.name)

@pytest.fixture(scope="function")
def client(test_db):
    def override_get_db():
        try:
            yield test_db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()
