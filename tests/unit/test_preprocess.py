import pytest
from io import BytesIO

def test_preprocess_image():
    """
    Test the preprocess_image function to ensure it processes images correctly.
    """
    from app.services.image_service.preprocess import preprocess_image
    from PIL import Image
    import numpy as np

    # Create a dummy image in memory and save it to bytes
    img = Image.new('RGB', (128, 128), color='red')
    img_bytes_io = BytesIO()
    img.save(img_bytes_io, format='JPEG')  # Gebruik JPEG of PNG
    img_bytes = img_bytes_io.getvalue()

    # Call the preprocess_image function
    preprocessed_image, resized_image_bytes = preprocess_image(img_bytes, target_size=(128, 128))

    # Check if the preprocessed image is a numpy array with the correct shape
    assert isinstance(preprocessed_image, np.ndarray), "Preprocessed image should be a numpy array"
    assert preprocessed_image.shape == (1, 128, 128, 3), "Preprocessed image shape should be (1, 128, 128, 3)"

    # Optioneel: check dat de bytes geen lege afbeelding opleveren
    assert isinstance(resized_image_bytes, bytes)
    assert len(resized_image_bytes) > 0
