
from app.services.preprocess_service import  preprocess_image
from app.core.store_result import store_result
from app.core.constants import  Config
from app.services.machine_learning_service import model_predict
from app.services.database_service.prediction_service import save_prediction
import logging

def process_image_to_result(image_bytes, filename, db):
    """
    Process the image bytes, predict the class and confidence score, and save the result.
    Args:
        image_bytes: The image bytes to process.
        filename: The name of the file. (to keep track of the image)
        db: The database session. 
    """
    try:
        preprocessed_image, image_bytes = preprocess_image(image_bytes, Config.PREPROCESS_SIZE, filename) 

        predicted_class, confidence_score = model_predict(preprocessed_image)
        store_result(filename, predicted_class, confidence_score)
        
        save_prediction(db, filename, predicted_class, confidence_score, image_bytes)
        logging.info(f"Predicted class: {predicted_class}, Confidence score: {confidence_score}")

    except Exception as e:
        raise ValueError(f"Error during image processing: {e}")