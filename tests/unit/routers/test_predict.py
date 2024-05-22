from fastapi import Request
import pytest
from fastapi.testclient import TestClient
from src.routers.predict import router  # Assuming `predict` is the name of your router
from src.models.models_monostate import IrisModelMonostate
@pytest.fixture
def client():
    """Create a TestClient instance for testing."""
    IrisModelMonostate()
    return TestClient(router)

def test_predict_iris(client: TestClient):
    """Test the predict_iris route."""
    # Mock input features
    features = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
 

    # Make request to predict_iris route
    response = client.post("/predict", json=features)
    
    # Check response status code
    assert response.status_code == 200

    # Check response data if necessary
