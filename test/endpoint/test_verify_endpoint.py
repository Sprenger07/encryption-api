from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_verify_no_json():
    response = client.post("/verify")
    assert response.status_code == 400


def test_verify_no_signature():
    response = client.post("/verify")
    assert response.status_code == 400


def test_verify_no_data():
    response = client.post("/verify")
    assert response.status_code == 400


def test_verify_valid_input():
    payload = {"message": "Hello World", "timestamp": 1616161616}
    response_sign = client.post("/sign", json=payload)
    assert response_sign.status_code == 200

    response_sign = client.post(
        "/verify",
        json={"signature": response_sign.json().get("signature"), "data": payload},
    )
    assert response_sign.status_code == 204
