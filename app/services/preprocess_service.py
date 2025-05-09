from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import tensorflow as tf

from PIL import Image
from app.core.constants import Paths  # of pas dit aan naar je eigen structuur

def preprocess_image(image_path, target_size, filename):
    """
    Preprocess the image for the model and save the preprocessed image.
    
    Args:
        image_path (str): Path to the original image.
        target_size (tuple): Target size for resizing the image.
    
    Returns:
        np.ndarray: Preprocessed image ready for model input.
        PIL.Image: The original resized image.
    """

    img = tf.keras.preprocessing.image.load_img(image_path, target_size=target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0

    # Sla de genormaliseerde afbeelding op
    img_to_save = (img_array * 255).astype(np.uint8)  # terugschalen
    img_pil = Image.fromarray(img_to_save)
    
    
    # save_path = f"{Paths.UPLOADS_PREPROCESSED}/{filename}"
    # img_pil.save(save_path)

    return np.expand_dims(img_array, axis=0), img
