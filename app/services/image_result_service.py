
from app.services.preprocess_service import  preprocess_image
from app.core.store_result import store_result
from app.core.constants import Paths, Config
from app.services.machine_learning_service import model_predict

def process_image_to_result(image_bytes, filename):
    """
    Prosess the image to get the result.
    This function uses the original preprocessing method (Without sam).
    It loads the image, preprocesses it, and predicts the class using the model.
    """
    try:
        preprocessed_image, img = preprocess_image(image_bytes, Config.PREPROCESS_SIZE, filename) 

        predicted_class, confidence_score = model_predict(preprocessed_image)
        store_result(filename, predicted_class, confidence_score)
        print(f"Predicted class: {predicted_class}, Confidence score: {confidence_score}")
        
    except Exception as e:
        raise ValueError(f"Error during image processing: {e}")