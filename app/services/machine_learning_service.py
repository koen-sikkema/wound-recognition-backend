from app.core.constants import Config
from app.core.ml_manager.model_manager import ModelManager
import numpy as np

def model_predict(image: np.ndarray):
    """Predict the class of the image using the pre-trained model."""
    
    model_manager = ModelManager()
    pred = model_manager.predict(image)
    
    predicted_idx = np.argmax(pred, axis=1)[0]
    labels = Config.get_labels()
    predicted_class = labels[predicted_idx]
    confidence_score = np.max(pred, axis=1)[0]

    return predicted_class, confidence_score


