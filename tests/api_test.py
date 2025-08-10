import pytest
from unittest.mock import patch

# Patch MlflowClient and pyfunc.load_model before importing app
with patch("mlflow.tracking.MlflowClient"), patch("mlflow.pyfunc.load_model"):
    from src.api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_predict_post_200(client):
    response = client.post("/predict", json={ "MedInc": 8.3252, "HouseAge": 41.0, "AveRooms": 6.9841, "AveBedrms": 1.0238, "Population": 322.0, "AveOccup": 2.5556, "Latitude": 37.88, "Longitude": -122.23})
    assert response.status_code == 200 

def test_predict_post_Error(client):
    response = client.post("/predict", json={ "test":1.0})
    data = response.get_json()
    assert "error" in data
    assert data["error"] # This checks that the value is not empty or falsy 