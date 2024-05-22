import pytest
from fastapi.testclient import TestClient
from src.routers.root import router  
from unittest.mock import MagicMock

@pytest.fixture
async def client():
    """Create a TestClient instance for testing."""
    return await TestClient(router)

async def test_docs_redirect(client):
    """Test the docs_redirect route."""
    # Make request to docs_redirect route
    response = await client.get("/")
    #print(response.status_code)
    # Check response status code
    # assert response.status_code == 307  # Expecting a temporary redirect
    print(response.json())
    # Check redirect URL
    assert response.headers["location"] == "/docs"