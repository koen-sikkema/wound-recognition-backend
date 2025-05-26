import numpy as np
import pytest
from unittest.mock import patch, MagicMock
from app.services.prediction_service.model_predictor import model_predict  

@patch("app.services.prediction_service.model_predictor.Config.get_labels")
@patch("app.services.prediction_service.model_predictor.ModelManager.get_instance")
def test_model_predict_success(mock_get_instance, mock_get_labels):
    """Test successful model prediction with mocked model manager and labels."""
    fake_prediction = np.array([[0.1, 0.7, 0.2]])  
    fake_labels = ["class_a", "class_b", "class_c"]

    mock_model_manager = MagicMock()
    mock_model_manager.predict.return_value = fake_prediction
    mock_get_instance.return_value = mock_model_manager
    mock_get_labels.return_value = fake_labels

    dummy_image = np.zeros((128, 128, 3), dtype=np.float32)


    predicted_class, confidence = model_predict(dummy_image)

    assert predicted_class == "class_b"
    assert confidence == 0.7
    mock_model_manager.predict.assert_called_once_with(dummy_image)
    mock_get_labels.assert_called_once()


@patch("app.services.prediction_service.model_predictor.ModelManager.get_instance")
def test_model_predict_exception(mock_get_instance):

    mock_model_manager = MagicMock()
    mock_model_manager.predict.side_effect = Exception("model failed")
    mock_get_instance.return_value = mock_model_manager

    dummy_image = np.zeros((128, 128, 3), dtype=np.float32)


    with pytest.raises(ValueError) as exc_info:
        model_predict(dummy_image)

    assert "Error during model prediction" in str(exc_info.value)
