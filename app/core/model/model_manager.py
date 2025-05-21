
import tensorflow as tf
from app.core.constants import Paths

class ModelManager:
    """
    Singleton class to manage the loading and initialization of the model.
    This class ensures that the model is loaded only once and can be reused.
    """
    _instance = None # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def initialize_model(self, ):
        """Initialize the model manager."""
        if not self._initialized:
            self.best_cnn = self.load_keras_model()
            self._initialized = True
            
    def load_keras_model(self):
        """Load the Keras model from the specified path."""
        
        return tf.keras.models.load_model(Paths.BEST_CNN_PATH, compile=False)

