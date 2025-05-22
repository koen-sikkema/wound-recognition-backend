import logging
from fastapi import BackgroundTasks, HTTPException, UploadFile
from app.services.prediction_service.prediction_pipeline import run_prediction_pipline
from sqlalchemy.orm import Session


def handle_upload(background_tasks: BackgroundTasks, file: UploadFile, db: Session):
    """
    Handle the file upload and process it in the background.
    Args:
        background_tasks: The background tasks to run.
        file: The uploaded file.
        db: The database session.
    Returns:
        dict: A message indicating the result of the upload.
    """
    try:
        logging.info(f"File {file.filename} uploaded successfully")
        image_bytes = file.file.read()
        background_tasks.add_task(run_prediction_pipline, image_bytes, file.filename, db)
        return {"message": "File uploaded successfully, processing in background"}
    except Exception as e:
        logging.error(f"Error uploading file: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="File upload failed")
