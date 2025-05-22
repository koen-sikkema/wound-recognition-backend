from app.core.constants import Config
from app.core.ml_manager.model_manager import ModelManager
import numpy as np
import logging

def model_predict(image: np.ndarray) -> tuple[str, float]:
    """
    Predict the class of the image using the pre-trained model.
    Args:
        image (np.ndarray): Preprocessed image ready for model input.
    Returns:
        tuple: A tuple containing the predicted class and confidence score.
    """
    
    try:
        model_manager = ModelManager.get_instance()
        pred = model_manager.predict(image)
        
        predicted_idx = np.argmax(pred, axis=1)[0]
        labels = Config.get_labels()
        predicted_class = labels[predicted_idx]
        confidence_score = np.max(pred, axis=1)[0]

        return predicted_class, confidence_score
    except Exception as e:
        logging.exception("Exception occurred during model prediction")
        raise ValueError(f"Error during model prediction: {e}")


