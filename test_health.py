from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {'status': 'OK'}


def test_create_explanation():
    response = client.post(
        "/explanation/",
        json={"manuscript_id": "1", "reviewer_id": "1"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "manuscript_id": "1",
        "reviewer_id": "1",
        "explanation": "Here's why...",
    }