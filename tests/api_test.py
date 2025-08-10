import pytest
from src.api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_predict_post(client):
    # Replace with actual expected input for your model
    response = client.post("/predict", json={"feature1": 1, "feature2": 2})
    assert response.status_code in (200, 400)  # Adjust as needed