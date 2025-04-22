# app/services/image_processing_service.py
from app.services.image_pipeline.image_segment_pipeline import segment_image
from app.services.image_pipeline.image_crop_pipeline import crop_image
from app.services.image_pipeline.image_preprocess_pipeline import preprocess_image

class ImageProcessingService:
    def __init__(self, manager):
        self.manager = manager  # De modelmanager die de modellen beheert.

    async def process_image(self, filename):
        """
        Verwerkt de afbeelding door segmentatie, cropping en preprocessen.
        """
        try:
            # Segmentatie
            image, mask, score = await segment_image(filename)

            # Croppen
            cropped_image = crop_image(filename, image, mask)

            # Preprocessen
            preprocessed_image = preprocess_image(filename, cropped_image)

            return preprocessed_image
        
        except Exception as e:
            raise ValueError(f"Error during image processing: {e}")
