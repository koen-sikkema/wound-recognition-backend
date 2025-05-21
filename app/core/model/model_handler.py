from app.core.model.model_manager import ModelManager

class ModelHandler:
    """
    Singleton class to handle the model loading and prediction.
    """
    MODEL_MANAGER = ModelManager()
