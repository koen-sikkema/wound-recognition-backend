from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.preprocessing.image import array_to_img

import numpy as np
import tensorflow as tf

from app.core.constants import Paths  # of pas dit aan naar je eigen structuur

def preprocess_image(image_path, target_size):
    """
    Preprocess the image for the model.
    """

    # Load and resize the image
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=target_size)

    # Convert to array and preprocess for the model
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    preprocessed_array = preprocess_input(img_array)

    # Convert original array (not preprocessed) to PIL image for display or other use
    pil_img = array_to_img(img_array)  # Note: use unprocessed array
    pil_img = pil_img.resize(target_size)

    return np.expand_dims(preprocessed_array, axis=0)

