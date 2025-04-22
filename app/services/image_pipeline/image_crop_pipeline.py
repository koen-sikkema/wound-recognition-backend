import numpy as np
import cv2
from app.core.constants import  Paths

def crop_image(filename: str, image: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """
    Crops the image using the bounding box of the mask.
    Saves the cropped image (with original colors) to uploads/mask/
    """
    print("cropping image...")

    # Convert mask to uint8 if needed
    if mask.dtype != np.uint8:
        mask = mask.astype(np.uint8)

    # Find bounding box
    coords = np.argwhere(mask)
    if coords.size == 0:
        raise ValueError("No non-zero mask pixels found.")

    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)

    # Crop original image based on mask bounding box
    cropped = image[y_min:y_max+1, x_min:x_max+1]

    save_path = f"{Paths.UPLOADS_PREPROCESSED}/{filename}"
    print(f"saving cropped...")
    cv2.imwrite(save_path, cropped)
    return cropped
