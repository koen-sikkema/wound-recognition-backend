# load model cnn
# from tensorflow.keras.models import load_model
from tensorflow.keras.models import load_model  
import numpy as np
from app.core.constants import Config, ModelHandler
import cv2
import os


def model_predict(image: np.ndarray, filename: str) -> str:
    # Load the model once when the module is imported

    pred = ModelHandler.MODEL_MANAGER.load_keras_model().predict(image)
    predicted_idx = np.argmax(pred, axis=1)[0]
    
    predicted_class = Config.LABELS[predicted_idx]
    confidence_score = np.max(pred, axis=1)[0]

    return predicted_class, confidence_score
    # Return the class index with the highest probability and the confidence score

 