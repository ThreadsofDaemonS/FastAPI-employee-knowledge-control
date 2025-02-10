from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)

def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }