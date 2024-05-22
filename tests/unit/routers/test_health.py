from fastapi.testclient import TestClient
import pytest

from src.routers.health import router

@pytest.fixture
def client():
    """Create a TestClient instance for testing."""
    return TestClient(router)

def test_health_endpoint(client):
    """Test the health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "API health: OK!"}