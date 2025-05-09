from fastapi.testclient import TestClient

from src.main import app

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

    name = response.json().get("name")
    assert name == "Sm9obiBEb2U="

    age = response.json().get("age")
    assert age == "MzA="

    contact = response.json().get("contact")
    assert contact.startswith("eyJlbWFpbCI6ImpvaG5AZXhhbXBsZS5j")
