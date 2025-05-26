from unittest.mock import patch

def test_upload_image(client, dummy_image_bytes):
    response = client.post(
        "/upload/",
        files={"file": ("test.jpg", dummy_image_bytes, "image/jpeg")}
    )
    assert response.status_code == 200
    assert "processing in background" in response.json()["message"]


def test_upload_image(client, dummy_image_bytes):
    with patch("app.services.image_service.preprocess") as mock_process_image:
        response = client.post(
            "/upload/",
            files={"file": ("test.jpg", dummy_image_bytes, "image/jpeg")}
        )
        assert response.status_code == 200
        assert "processing in background" in response.json()["message"]
        mock_process_image.assert_not_called()  

def test_get_result_route(client, dummy_image_bytes):
    """Test the result retrieval route."""

    response = client.post(
        "/upload/",
        files={"file": ("test.jpg", dummy_image_bytes, "image/jpeg")}
    )
    response = client.get("/results/?filename=test.jpg")
    assert response.status_code == 200
    assert "filename" in response.json()
    assert response.json()["filename"] == "test.jpg"

def test_get_result_route_not_found(client):
    """Test the result retrieval route for a non-existent file."""
    response = client.get("/results/?filename=non_existent.jpg")
    assert response.status_code == 202
    assert "message" in response.json()
    assert response.json()["message"] == "Result not yet available"

def test_get_result_route_invalid_filename(client):
    """Test the result retrieval route with an invalid filename."""
    response = client.get("/results/?filename=")
    assert response.status_code == 202
    assert response.json()["message"] == "Result not yet available"

def test_read_all_route(client):
    """Test the read all route."""
    response = client.get("/predictions/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict), "Response should be a dictionary"
    assert "predictions" in data, "'predictions' key should be in the response"
    assert isinstance(data["predictions"], list), "'predictions' should be a list"

def test_delete_all_predictions(client):
    """Test the delete all predictions route."""
    response = client.delete("/predictions/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "All predictions deleted successfully."