
import numpy as np
import cv2
from PIL import Image

def crop_image(image: np.ndarray, mask: np.ndarray) -> np.ndarray:

    """
    Crop and resize an image based on a binary mask from SAM(segment anything now).
    The function finds the bounding box of the mask and crops the image accordingly.
    Args:
        image (np.ndarray): The input image to crop.
        mask (np.ndarray): The binary mask to use for cropping.
    Returns:
        np.ndarray: The cropped image.
    
    """
    # find the bounding box of the mask
    coords = np.argwhere(mask)
    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)

    # Crop =the image
    cropped = image[y_min:y_max+1, x_min:x_max+1]

    return Image.fromarray(cropped)