from src.services.encryption_service import Encrypter
from src.services.decryption_service import Decrypter

encrypter = Encrypter()
decrypter = Decrypter()


def test_encode_decode_value_string():
    value = "Jhon Doe"

    encoded_value = encrypter.encode(value)
    decoded_value = decrypter.decode(encoded_value)
    assert decoded_value == value


def test_encode_decode_value_int():
    value = 30
    encoded_value = encrypter.encode(value)
    decoded_value = decrypter.decode(encoded_value)
    assert decoded_value == value


def test_encode_decode_value_list():
    value = ["hello", "word"]

    encoded_value = encrypter.encode(value)
    decoded_value = decrypter.decode(encoded_value)
    assert decoded_value == value


def test_encode_decode_value_dictionary():
    value = {"age": 30, "name": "Jhon Doe"}

    encoded_value = encrypter.encode(value)
    decoded_value = decrypter.decode(encoded_value)
    assert decoded_value == value


def test_encode_decode_value_none():
    value = None

    encoded_value = encrypter.encode(value)
    decoded_value = decrypter.decode(encoded_value)
    assert decoded_value == value
