
from app.services.image_service.preprocess import  preprocess_image
from app.services.prediction_service.cache_handler import cache_prediction
from app.core.constants import  Config
from app.services.prediction_service.model_predictor import model_predict
from app.services.prediction_service.prediction_storage import store_prediction_to_db 
import logging
from sqlalchemy.orm import Session

def run_prediction_pipline(image_bytes: bytes, filename: str, db: Session):
    """
    Run the complete pipeline: preprocess → predict → store → cache.
        
    Args:
        image_bytes: The image bytes to process.
        filename: The name of the file (to keep track of the image).
        db: The database session.
    """
    try:
        preprocessed_image, image_bytes = preprocess_image(image_bytes, Config.PREPROCESS_SIZE, filename) 

        predicted_class, confidence_score = model_predict(preprocessed_image)
        cache_prediction(filename, predicted_class, confidence_score)
        
        store_prediction_to_db(db, filename, predicted_class, confidence_score, image_bytes)
        logging.info(f"Predicted class: {predicted_class}, Confidence score: {confidence_score}")

    except Exception as e:
        logging.error(f"Prediction pipeline failed for {filename}: {e}", exc_info=True)
        raise ValueError(f"Error during image processing: {e}")