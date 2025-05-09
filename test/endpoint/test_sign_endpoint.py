from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_sign_no_json():
    response = client.post("/sign")
    assert response.status_code == 400


def test_sign_with_empty_json():
    response = client.post("/sign", json={})
    assert response.status_code == 200


def test_sign_with_different_property_order_json():
    response_1 = client.post(
        "/sign", json={"message": "Hello World", "timestamp": 1616161616}
    )

    response_2 = client.post(
        "/sign", json={"timestamp": 1616161616, "message": "Hello World"}
    )
    assert response_1.status_code == 200
    assert response_1.json().get("signature") == response_2.json().get("signature")
