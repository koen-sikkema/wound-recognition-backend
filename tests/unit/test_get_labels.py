import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from app.core.constants import Paths, get_prediction_labels

def test_get_prediction_labels_success():
    """Test successful loading of labels from CSV."""
    dummy_df = pd.DataFrame({"Class": ["label1", "label2", "label3"]})

    with patch.object(Paths.LABELS_CSV_NL, "exists", return_value=True), \
         patch("app.core.utils.pd.read_csv", return_value=dummy_df) as mock_read_csv:
        
        labels = get_prediction_labels()

        mock_read_csv.assert_called_once_with(Paths.LABELS_CSV_NL)
        assert labels == ["label1", "label2", "label3"], "Labels should match the dummy DataFrame"
        

def test_get_prediction_labels_file_missing():
    """Test that a FileNotFoundError is raised if CSV does not exist."""
    with patch.object(Paths.LABELS_CSV_NL, "exists", return_value=False):
        with pytest.raises(FileNotFoundError) as exc_info:
            get_prediction_labels()
        
        assert "Labels CSV not found" in str(exc_info.value) 
