from segment_anything import SamPredictor, sam_model_registry
import cv2
import numpy as np


sam_weights = r'C:\Users\koens\Documents\GitHub\wound-recognition-backend\SAM_weights/sam_vit_b_01ec64.pth' 

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
    # Load the model
    print("loading model...")
    sam = sam_model_registry["vit_b"](checkpoint=sam_weights)
    predictor = SamPredictor(sam)
    print("model loaded\n loading image...")

    # Read and set the image
    image = cv2.imread(filepath)

    if image is None:
        print(f"Error: Unable to load image at {filename}")
    else:
        print(f"Image loaded successfully: {filename}")

    predictor.set_image(image)
    print("image loaded\n predicting mask...")
    # Get image center as point prompt
    height, width, _ = image.shape
    input_point = np.array([[width // 2, height // 2]])
    input_label = np.array([1])  # 1 betekent foreground

    # Predict the mask using the center point
    masks, scores, logits = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=False
    )
    print("mask predicted\n processing mask...")
    # Optioneel: alleen de beste mask teruggeven
    mask = masks[0] #numpy.ndarray
    score = scores[0]

    return image, mask, score

