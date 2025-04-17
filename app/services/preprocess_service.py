import numpy as np
from PIL import Image

def preprocess_image(image: Image.Image, size=(128, 128)) -> np.ndarray:
    """
    preprocess_image: Resize and normalize an image for CNN input.
    The image is resized to the specified size and normalized to the range [0, 1].
    The image is reshaped to include a batch dimension.
    Args:
        image (Image.Image): The input image to preprocess.
        size (tuple): The target size for the image (height, width). Default is (128, 128).
    Returns:
        np.ndarray: The preprocessed image ready for CNN input.
    """
    image = image.resize(size)  # als het al gesized is, hoeft dit niet
    image = np.array(image) / 255.0
    return image.reshape((1, size[0], size[1], 3))
