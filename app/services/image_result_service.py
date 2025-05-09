
from app.core.store_result import store_result
from app.core.constants import Paths, Config
from app.services.machine_learning_service import model_predict
from app.services.image_pipeline.image_preprocess_pipeline import preprocess_image
from app.services.image_pipeline.image_segment_pipeline import segment_image
from app.services.image_pipeline.image_crop_pipeline import crop_and_resize_image

def process_image_to_result(filename):
    """
    Prosess the image to get the result.
    """ 
    try:
        # Preprocess
        segmented_image, mask, score = segment_image(filename) 

        # Hier ben je bezig met de segmentatie van de afbeelding

        cropped_image, image_path = crop_and_resize_image(filename, segmented_image, mask)
        # predict 
        preprocessed_image = preprocess_image(image_path, target_size=Config.PREPROCESS_SIZE)
        predicted_class, confidence_score = model_predict(preprocessed_image)
        store_result(filename, predicted_class, confidence_score)
        print(f"Predicted class: {predicted_class}, Confidence score: {confidence_score}")
        
    except Exception as e:
        raise ValueError(f"Error during image processing: {e}")