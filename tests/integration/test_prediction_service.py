from app.services.prediction_service.prediction_pipeline import run_prediction_pipline
from app.services.prediction_service.cache_handler import get_cached_prediction
def test_run_prediction_pipeline_integration(dummy_image_bytes, test_db):
    filename = "integration_test_image.png"
    
    # initialize the model 
    from app.core.ml_manager.model_manager import ModelManager 
    ModelManager.get_instance().initialize_model()
    run_prediction_pipline(dummy_image_bytes, filename, test_db)

    from app.core.constants import Config
    cached_result = get_cached_prediction(filename)
    assert cached_result is not None, "Prediction not cached"
    filename = cached_result.filename
    label = cached_result.label
    confidence = cached_result.confidence
    assert label in Config.get_labels()
    assert 0.0 <= confidence <= 1.0

    
    from app.core.database_models.prediction import Prediction
    prediction = test_db.query(Prediction).filter_by(filename=filename).first()
    assert prediction is not None, "Prediction not stored in DB"
    assert abs(prediction.confidence - confidence) < 1e-5
