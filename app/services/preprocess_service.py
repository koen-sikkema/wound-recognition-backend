from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import tensorflow as tf
from app.core.constants import Paths, Config


def preprocess_image(image_path, target_size):
    """
    Preprocess the image for the model.
    This function loads the image, resizes it to the target size,
    normalizes it, and expands the dimensions to match the model input shape.
    
    args:
        image_path (str): Path to the image file.
        target_size (tuple): Target size for resizing the image.

    returns:
        np.ndarray: Preprocessed image ready for model input.
    """

    img = tf.keras.preprocessing.image.load_img(image_path, target_size=target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0
    return np.expand_dims(img_array, axis=0), img