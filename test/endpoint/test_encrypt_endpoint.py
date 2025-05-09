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


def test_encrypt_with_string_instead_of_int():
    response = client.post(
        "/encrypt",
        json={
            "name": "John Doe",
            "age": "30",
            "contact": {"email": "john@example.com", "phone": "123-456-7890"},
        },
    )
    assert response.status_code == 200

    age = response.json().get("age")
    assert age == "MzA="


def test_encrypt_with_list():
    response = client.post(
        "/encrypt",
        json={
            "hello_word_list": ["hello", "word"],
            "hello_word_str": "['hello', 'word']",
        },
    )
    assert response.status_code == 200

    encrypted_hello_word_list = response.json().get("hello_word_list")
    encrypted_hello_word_str = response.json().get("hello_word_str")
    assert encrypted_hello_word_list != encrypted_hello_word_str


def test_encrypt_with_bool():
    response = client.post(
        "/encrypt",
        json={"True": True, "False": False},
    )
    assert response.status_code == 200

    encrypted_true = response.json().get("True")
    assert encrypted_true == "VHJ1ZQ=="

    encrypted_false = response.json().get("False")
    assert encrypted_false == "RmFsc2U="


def test_encrypt_with_none():
    response = client.post(
        "/encrypt",
        json={
            "None": None,
        },
    )
    assert response.status_code == 200

    encrypted_none = response.json().get("None")
    assert encrypted_none == "Tm9uZQ=="
