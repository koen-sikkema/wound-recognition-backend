# load model cnn
# from tensorflow.keras.models import load_model
from tensorflow.keras.models import load_model  
import numpy as np
import cv2
import os

async def predict_cnn(image: np.ndarray) -> str:
# Load the model once when the module is imported
    model_path = os.path.join(os.path.dirname(__file__), 'best_cnn.h5')
    model = load_model(model_path)
    print("CNN model loaded successfully")
    prediction = model.predict(image)
    return prediction.argmax(axis=1)[0]  # Return the class index with the highest probability

 