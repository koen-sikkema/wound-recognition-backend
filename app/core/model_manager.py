import os
import tensorflow as tf
import torch
from tensorflow.keras.models import load_model
from segment_anything import SamPredictor, sam_model_registry
from app.core.constants import Paths, Config

class ModelManager:
    _instance = None # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelManager, cls).__new__(cls)
            cls._instance._intialized = False
        return cls._instance
    
    def initialize_model(self, keras_model_path, sam_checkpoint_path, sam_model_type):
        """Initialize the model manager."""
        if not self._initialized:
            self.best_cnn = self.load_keras_model()
            self.sam_predicter = self.load_sam_model() 
            self._initialized = True
            
    def load_keras_model(self):
        """
        Loads a TensorFlow Keras model from the given file path.
        """
        print("loading best cnn...")
        return tf.keras.models.load_model(Paths.BEST_CNN_PATH, compile=False)
    
    def load_sam_model(self):
        """
        Loads a SAM model from the given file path.
        """
        print("loading sam...")
        sam = sam_model_registry[Config.SAM_TYPE_VIT_B](checkpoint=Paths.SAM_WEIGHTS)
        sam.to(device="cuda" if torch.cuda.is_available() else "cpu")
        return SamPredictor(sam)
    

