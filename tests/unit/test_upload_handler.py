import pytest
from fastapi import UploadFile, BackgroundTasks
from io import BytesIO
from unittest.mock import MagicMock
from app.services.image_service.upload_handler import handle_upload

def test_handle_upload_dummy():
    """
    Test the upload handler with mocked dependencies.
    """
    file_content = b"dummy image content"
    file = UploadFile(filename="test_image.jpg", file=BytesIO(file_content))

    background_tasks = BackgroundTasks()
    db = MagicMock()  

    result = handle_upload(background_tasks, file, db)

    assert "message" in result
    assert result["message"].startswith("File uploaded successfully")
