from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
from io import BytesIO
import tensorflow as tf

from PIL import Image
from app.core.constants import Paths  # of pas dit aan naar je eigen structuur

def preprocess_image(image_bytes, target_size):
    """
    Preprocess the image for the model and save the preprocessed image.
    
    Args:
        image_path (str): Path to the original image.
        target_size (tuple): Target size for resizing the image.
    
    Returns:
        np.ndarray: Preprocessed image   ready for model input.
        PIL.Image: The original resized image.
    """

    image = load_img(BytesIO(image_bytes), target_size=target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(image) /255.0

    return np.expand_dims(img_array, axis=0), image_bytes
