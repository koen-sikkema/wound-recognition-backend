import pytest
import numpy as np
from app.core.ml_manager.model_manager import ModelManager
from unittest.mock import patch, MagicMock

def test_model_manager_singleton():
    """
    Test that the ModelManager is a singleton.
    """
    instance1 = ModelManager.get_instance()
    instance2 = ModelManager.get_instance()
    assert instance1 is instance2, "ModelManager should be a singleton"

def test_initialize_model():
    """
    Test that the model is initialized correctly.
    """
    # Reset singleton instance before patch
    ModelManager._instance = None

    with patch.object(ModelManager, 'load_keras_model', return_value=MagicMock()) as mock_load:
        model_manager = ModelManager.get_instance()  # get after patch
        model_manager.initialize_model()

        mock_load.assert_called_once()
        assert model_manager.best_cnn is not None, "Model should be initialized"
        assert model_manager._initialized is True, "Model should be marked as initialized"

def test_initialize_model_already_initialized():
    """
    Test that the model is not re-initialized if already initialized.
    """
    ModelManager._instance = None
    with patch.object(ModelManager, 'load_keras_model') as mock_load:
        manager = ModelManager.get_instance()
        manager._initialized = True  # Simuleer dat model al geladen is
        manager.initialize_model()

        mock_load.assert_not_called()

def test_predict():
    """
    Test that the predict method works correctly.
    """
    # Reset singleton instance before patch
    ModelManager._instance = None

    model_manager = ModelManager.get_instance()
    model_manager.initialize_model()

    mock_model = MagicMock()
    model_manager.best_cnn = mock_model

    test_image = np.random.rand(128, 128, 3)  # Dummy image
    mock_model.predict.return_value = np.array([[0.1, 0.9]])  # Dummy prediction

    prediction = model_manager.predict(test_image)

    mock_model.predict.assert_called_once_with(test_image)
    assert np.array_equal(prediction, np.array([[0.1, 0.9]])), "Prediction should match the mocked value"

def test_predict_model_not_initialized():
    """
    Test that an error is raised if the model is not initialized.
    """
    # Reset singleton instance before patch
    ModelManager._instance = None

    model_manager = ModelManager.get_instance()
    with pytest.raises(RuntimeError, match="Model not initialized"):
        model_manager.predict(np.random.rand(128, 128, 3))

