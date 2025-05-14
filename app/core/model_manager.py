import os
import tensorflow as tf
import torch
from tensorflow.keras.models import load_model
from app.core.constants import Paths, Config

class ModelManager:
    _instance = None # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def initialize_model(self, keras_model_path):
        """Initialize the model manager."""
        if not self._initialized:
            self.best_cnn = self.load_keras_model()
            self._initialized = True
            
    def load_keras_model(self):
        """
        Loads a TensorFlow Keras model from the given file path.
        """
        print("loading cnn...")
        return tf.keras.models.load_model(Paths.BEST_CNN_PATH, compile=False)

