import logging
from fastapi import BackgroundTasks
from app.services.image_result_service import process_image_to_result

def handle_upload(background_tasks: BackgroundTasks, file):
    try:
        logging.info(f"File {file.filename} uploaded successfully")
        image_bytes = file.file.read()
        background_tasks.add_task(process_image_to_result, image_bytes, file.filename)
        return {"message": "File uploaded successfully, processing in background"}
    except Exception as e:
        logging.error(f"Error uploading file: {e}", exc_info=True)
        raise e
