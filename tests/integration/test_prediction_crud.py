from app.crud.prediction_crud import (
    save_prediction,
    get_prediction,
    delete_prediction,
    delete_all_predictions,
    get_all_predictions,
)
from app.core.database_models.prediction import Prediction

def test_save_and_get_prediction(test_db):
    """
    Test saving a prediction and then retrieving it.
    """
    result = save_prediction(
        db=test_db,
        filename="test1.png",
        label="Brandwond",
        confidence=0.95,
        wound_image=b"dummybytes",
    )

    assert result.id is not None
    assert result.filename == "test1.png"
    assert result.label == "Brandwond"

    fetched = get_prediction(test_db, "test1.png")
    assert fetched is not None
    assert fetched.id == result.id


def test_delete_prediction(test_db):
    """
    Test deleting a prediction.
    """
    save_prediction(test_db, "test2.png", "Brandwond", 0.8, b"dummybytes")
    deleted = delete_prediction(test_db, "test2.png")
    assert deleted is True
    # If we try to delete it again, it should return False because it no longer exists
    deleted_again = delete_prediction(test_db, "test2.png")
    assert deleted_again is False


def test_delete_all_predictions(test_db):
    """
    Test deleting all predictions.
    """
    save_prediction(test_db, "a.png", "Brandwond", 0.9, b"dummybytes")
    save_prediction(test_db, "b.png", "Normaal", 0.1, b"dummybytes")
    delete_all_predictions(test_db)

    predictions = get_all_predictions(test_db)
    assert predictions == []


def test_get_all_predictions(test_db):
    """
    Test getting all predictions.
    """
    save_prediction(test_db, "a.png", "Brandwond", 0.9, b"1")
    save_prediction(test_db, "b.png", "Normaal", 0.1, b"2")

    results = get_all_predictions(test_db)
    assert len(results) == 2
    filenames = [r["filename"] for r in results]
    assert "a.png" in filenames and "b.png" in filenames
