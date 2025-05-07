from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_encrypt_no_json():
    response = client.post("/encrypt")
    assert response.status_code == 400


def test_encrypt_empty_json():
    response = client.post("/encrypt", json={})
    assert response.status_code == 200


def test_encrypt_jhon_doe_example():
    response = client.post(
        "/encrypt",
        json={
            "name": "John Doe",
            "age": 30,
            "contact": {"email": "john@example.com", "phone": "123-456-7890"},
        },
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.get("name") == "Sm9obiBEb2U="
    assert response_json.get("age") == "MzA="
    assert response_json.get("contact").startswith("eyJlbWFpbCI6ImpvaG5AZXhhbXBsZS5j")
