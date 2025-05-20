
from tensorflow.keras.models import load_model  
import numpy as np
from app.core.constants import Config
from app.core.model.model_handler import ModelHandler

def model_predict(image: np.ndarray) -> str:
    """ 
    Predict the class of the image using the pre-trained model.
    """

    pred = ModelHandler.MODEL_MANAGER.load_keras_model().predict(image)
    predicted_idx = np.argmax(pred, axis=1)[0]
    
    predicted_class = Config.LABELS[predicted_idx]
    confidence_score = np.max(pred, axis=1)[0]

    return predicted_class, confidence_score


 