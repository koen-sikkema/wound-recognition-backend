import numpy as np
import cv2
from app.core.constants import Paths


def preprocess_image(filename: str, image: np.ndarray, size) -> np.ndarray:
    """
    preprocess_image: Resize and normalize an image for CNN input.
    The image is resized to the specified size and normalized to the range [0, 1].
    The image is reshaped to include a batch dimension.
    args:
        filename (str): The name of the image file.
        image (np.ndarray): The image to preprocess.
        size (tuple): The target size for resizing the image.
    returns:
        np.ndarray: The preprocessed image ready for CNN input.
    """

    print(f"Preprocessing image: {image.shape} -> {size}")
    
    if image.shape[:2] != size:
        print(f"Resizing image from {image.shape[:2]} to {size}")
        image_resized = cv2.resize(image, size)
    else:
        image_resized = image

    image_normalized = image_resized / 255.0
    print("Image normalized")

    save_path = f"{Paths.UPLOADS_PREPROCESSED}/{filename}"
    cv2.imwrite(save_path, (image_resized).astype(np.uint8))  # save RGB image, not normalized
    print(f"Saved preprocessed image to {save_path}")

    return image_normalized.reshape((1, size[0], size[1], 3))


