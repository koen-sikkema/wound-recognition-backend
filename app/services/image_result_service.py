# app/services/image_processing_service.py
from app.services.image_pipeline.image_segment_pipeline import segment_image
from app.services.image_pipeline.image_crop_pipeline import crop_image
from app.services.image_pipeline.image_preprocess_pipeline import preprocess_image
from app.core.store_result import store_result
from app.services.machine_learning_service import model_predict

def process_image_to_result(filename):
    """
    Verwerkt de afbeelding door segmentatie, cropping en preprocessen.
    """
    try:
        # Segmentation
        image, mask, score = segment_image(filename)

        # Crop
        cropped_image = crop_image(filename, image, mask)

        # Preprocess
        preprocessed_image = preprocess_image(filename, cropped_image)

        # predict 
        predicted_class, confidence_score = model_predict(preprocessed_image, filename)
        store_result(filename, predicted_class, confidence_score)
        print(f"Predicted class: {predicted_class}, Confidence score: {confidence_score}")
    except Exception as e:
        raise ValueError(f"Error during image processing: {e}")
