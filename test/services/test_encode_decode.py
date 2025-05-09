from src.services.encryption_service import Encoder
from src.services.decryption_service import Decoder

encoder = Encoder()
decoder = Decoder()


def test_encode_decode_value_string():
    value = "Jhon Doe"

    encoded_value = encoder.encode(value)
    decoded_value = decoder.decode(encoded_value)
    assert decoded_value == value


def test_encode_decode_value_int():
    value = 30
    encoded_value = encoder.encode(value)
    decoded_value = decoder.decode(encoded_value)
    assert decoded_value == value


def test_encode_decode_value_list():
    value = ["hello", "word"]

    encoded_value = encoder.encode(value)
    decoded_value = decoder.decode(encoded_value)
    assert decoded_value == value


def test_encode_decode_value_dictionary():
    value = {"age": 30, "name": "Jhon Doe"}

    encoded_value = encoder.encode(value)
    decoded_value = decoder.decode(encoded_value)
    assert decoded_value == value


def test_encode_decode_value_none():
    value = None

    encoded_value = encoder.encode(value)
    decoded_value = decoder.decode(encoded_value)
    assert decoded_value == value

