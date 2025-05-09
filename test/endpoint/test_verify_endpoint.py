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

    response_verify = client.post(
        "/verify",
        json={"signature": response_sign.json().get("signature"), "data": payload},
    )
    assert response_verify.status_code == 204


def test_verify_invalid_input():
    sign_payload = {"message": "Hello World", "timestamp": 1616161616}
    response_sign = client.post("/sign", json=sign_payload)
    assert response_sign.status_code == 200

    verify_payload = sign_payload
    verify_payload.update({"message": "Goodbye World"})
    response_verify = client.post(
        "/verify",
        json={
            "signature": response_sign.json().get("signature"),
            "data": verify_payload,
        },
    )
    assert response_verify.status_code == 400
