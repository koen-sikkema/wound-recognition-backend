
import tensorflow as tf
import numpy as np
from app.core.constants import Paths

class ModelManager:
    """
    Singleton class to manage the loading and initialization of the model.
    This class ensures that the model is loaded only once and can be reused.
    """
    _instance = None # Singleton instance

    def __new__(cls) -> "ModelManager":
        """Create a new instance of ModelManager if it doesn't exist."""
        if cls._instance is None:
            cls._instance = super(ModelManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def initialize_model(self) -> None:
        """Initialize the model manager."""
        if not self._initialized:
            self.best_cnn = self.load_keras_model()
            self._initialized = True
            
    def load_keras_model(self) -> tf.keras.Model:
        """Load the Keras model from the specified path."""
        
        return tf.keras.models.load_model(Paths.BEST_CNN_PATH, compile=False)
    
    def predict(self, image: np.ndarray) -> np.ndarray:
        """
        Predict the class of the image using the pre-trained model.
        Args:
            image (np.ndarray): Preprocessed image ready for model input.
        """
        if not self._initialized:
            raise RuntimeError("Model not initialized")
        pred = self.best_cnn.predict(image)
        return pred
    
    @classmethod
    def get_instance(cls) -> "ModelManager":
        """Get the singleton instance of ModelManager."""
        return cls()