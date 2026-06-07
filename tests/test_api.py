from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_check_endpoint():

    response = client.post(
        "/check",
        json={
            "text": "97% of users definitely prefer this."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "verdict" in data
    assert "checks" in data