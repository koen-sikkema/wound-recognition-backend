
from tensorflow.keras.models import load_model  
import numpy as np
from app.core.constants import Config, ModelHandler

def model_predict(image) -> tuple:
    """ 
    Predict the class of the image using the pre-trained model.
    """

    pred = ModelHandler.MODEL_MANAGER.load_keras_model().predict(image)
    predicted_idx = np.argmax(pred, axis=1)[0]
    
    predicted_class = Config.LABELS[predicted_idx]
    confidence_score = np.max(pred, axis=1)[0]

    return predicted_class, confidence_score
    # Return the class index with the highest probability and the confidence score

 