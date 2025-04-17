
import numpy as np
import cv2

def crop_and_resize(image: np.ndarray, mask: np.ndarray, size=(128, 128)) -> np.ndarray:
    # Vind de coördinaten waar mask True is
    coords = np.argwhere(mask)
    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)

    # Crop de afbeelding
    cropped = image[y_min:y_max+1, x_min:x_max+1]

    # Resize naar gewenste outputgrootte
    resized = cv2.resize(cropped, size, interpolation=cv2.INTER_AREA)

    return resized