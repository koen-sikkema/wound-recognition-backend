import cv2
import numpy as np
from segment_anything import SamPredictor, sam_model_registry

SAM_WEIGHTS = r'C:\Users\koens\Documents\GitHub\wound-recognition-backend\SAM_weights/sam_vit_b_01ec64.pth' 

async def segment_image(filename: str):
    """
    Asynchronously segment an image using the Segment Anything Model (SAM),
    assuming the wound is in the center of the image.
    The function loads the model, reads the image, and predicts the mask.

    Args:
        filename (str): The name of the image file to be segmented.
    Returns:
        tuple: A tuple containing the original image, the predicted mask, and the score.
    """

    filepath = f"uploads/raw_uploads/{filename}"

    print("loading model...")
    sam = sam_model_registry["vit_b"](checkpoint=SAM_WEIGHTS)
    predictor = SamPredictor(sam)
    
    print("loading image...")
    image = cv2.imread(filepath)
    if image is None:
        raise ValueError(f"Could not load image at {filepath}")
    print("image loaded")

    predictor.set_image(image)

    height, width, _ = image.shape
    input_point = np.array([[width // 2, height // 2]])
    input_label = np.array([1])

    masks, scores, _ = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=False
    )

    mask = masks[0]  # boolean mask
    score = scores[0]

    print("mask generated")
    return image, mask, score
