from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_decrypt_no_json():
    response = client.post("/decrypt")
    assert response.status_code == 400


def test_decrypt_empty_json():
    response = client.post("/decrypt", json={})
    assert response.status_code == 200


def test_decrypt_name_and_age():
    response = client.post("/decrypt", json={"name": "Sm9obiBEb2U=", "age": "MzA="})
    assert response.status_code == 200
    name = response.json().get("name")
    assert name == "John Doe"

    age = response.json().get("age")
    assert age == 30


def test_decrypt_with_crypted_dictionary():
    response = client.post(
        "/decrypt",
        json={
            "name": "Sm9obiBEb2U=",
            "age": "MzA=",
            "contact": "eyJlbWFpbCI6ImpvaG5AZXhhbXBsZS5jb20iLCJwaG9uZSI6IjEyMy00NTYtNzg5MCJ9",
        },
    )
    assert response.status_code == 200
    name = response.json().get("name")
    assert name == "John Doe"

    age = response.json().get("age")
    assert age == 30

    contact = response.json().get("contact")
    assert contact == {"email": "john@example.com", "phone": "123-456-7890"}


def test_decrypt_with_no_crypted_date():
    response = client.post(
        "/decrypt",
        json={
            "name": "Sm9obiBEb2U=",
            "age": "MzA=",
            "contact": "eyJlbWFpbCI6ImpvaG5AZXhhbXBsZS5jb20iLCJwaG9uZSI6IjEyMy00NTYtNzg5MCJ9",
            "birth_date": "1998-11-19",
        },
    )
    assert response.status_code == 200
    name = response.json().get("name")
    assert name == "John Doe"

    age = response.json().get("age")
    assert age == 30

    contact = response.json().get("contact")
    assert contact == {"email": "john@example.com", "phone": "123-456-7890"}

    birth_date = response.json().get("birth_date")
    assert birth_date == "1998-11-19"


def test_decrypt_with_encrypt_endpoint():
    payload = {
        "name": "user",
        "age": 42,
        "contact": "098-765-4321",
    }

    encrypt_response = client.post(
        "/encrypt",
        json=payload,
    )
    assert encrypt_response.status_code == 200
    encrypted_payload = encrypt_response.json()

    decrypt_response = client.post("/decrypt", json=encrypted_payload)
    assert decrypt_response.json() == payload


def test_decrypt_with_encrypt_endpoint_with_string_instead_of_int():
    payload = {
        "name": "user",
        "age": "42",
        "contact": "098-765-4321",
    }

    encrypt_response = client.post(
        "/encrypt",
        json=payload,
    )
    assert encrypt_response.status_code == 200
    encrypted_payload = encrypt_response.json()

    decrypt_response = client.post("/decrypt", json=encrypted_payload)
    assert decrypt_response.json() == payload


def test_decrypt_with_encrypt_endpoint_with_list():
    payload = {"hello_word ": ["hello", "word"]}

    encrypt_response = client.post(
        "/encrypt",
        json=payload,
    )
    assert encrypt_response.status_code == 200
    encrypted_payload = encrypt_response.json()

    decrypt_response = client.post("/decrypt", json=encrypted_payload)
    assert decrypt_response.json() == payload


def test_decrypt_with_encrypt_endpoint_with_boolean():
    payload = {"True": True, "False": False}

    encrypt_response = client.post(
        "/encrypt",
        json=payload,
    )
    assert encrypt_response.status_code == 200
    encrypted_payload = encrypt_response.json()

    decrypt_response = client.post("/decrypt", json=encrypted_payload)
    assert decrypt_response.json() == payload


def test_decrypt_with_encrypt_endpoint_with_None():
    payload = {
        "None": None,
    }

    encrypt_response = client.post(
        "/encrypt",
        json=payload,
    )
    assert encrypt_response.status_code == 200
    encrypted_payload = encrypt_response.json()

    decrypt_response = client.post("/decrypt", json=encrypted_payload)
    assert decrypt_response.json() == payload
