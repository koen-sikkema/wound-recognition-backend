import numpy as np
import cv2
from app.core.constants import Paths

def crop_and_resize_image(filename: str, image: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """
    Crops the image using the bounding box of the mask and resizes it
    to the original image dimensions with padding if needed to preserve aspect ratio.
    """
    print("Cropping and resizing image...")

    if mask.dtype != np.uint8:
        mask = mask.astype(np.uint8)

    coords = np.argwhere(mask)
    if coords.size == 0:
        raise ValueError("No non-zero mask pixels found.")

    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)

    cropped = image[y_min:y_max + 1, x_min:x_max + 1]
    cropped_mask = mask[y_min:y_max + 1, x_min:x_max + 1]

    # Resize keeping aspect ratio, with padding
    target_h, target_w = image.shape[:2]
    cropped_h, cropped_w = cropped.shape[:2]
    scale = min(target_w / cropped_w, target_h / cropped_h)
    resized = cv2.resize(cropped, (int(cropped_w * scale), int(cropped_h * scale)))

    # Add padding to match target size
    pad_vert = target_h - resized.shape[0]
    pad_horiz = target_w - resized.shape[1]
    top = pad_vert // 2
    bottom = pad_vert - top
    left = pad_horiz // 2
    right = pad_horiz - left

    padded = cv2.copyMakeBorder(resized, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    # Optional: overlay mask in blauw
    blue_mask = np.zeros_like(cropped)
    blue_mask[cropped_mask == 1] = [255, 0, 0]
    overlay = cv2.addWeighted(cropped, 0.8, blue_mask, 0.2, 0)

    # Resize and pad overlay the same way
    resized_overlay = cv2.resize(overlay, (resized.shape[1], resized.shape[0]))
    padded_overlay = cv2.copyMakeBorder(resized_overlay, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    save_path = f"{Paths.UPLOADS_MASKED}/{filename}"
    cv2.imwrite(save_path, padded_overlay)
    save_path = f"{Paths.UPLOADS_MASKED}/{filename}"
    cv2.imwrite(save_path, padded)

    return padded , save_path
