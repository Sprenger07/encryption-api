import base64
import json
from typing import Dict


class Decrypter:
    def decoding_algo(self, value) -> bytes:
        return base64.b64decode(value, validate=True)

    def decode(self, value) -> str | list | dict | int | None:
        try:
            decoded_value = self.decoding_algo(value)
            try:
                return json.loads(decoded_value)
            except Exception:
                if decoded_value == b"None":
                    return None
                if decoded_value == b"True":
                    return True
                if decoded_value == b"False":
                    return False
                return decoded_value.decode("utf-8")
        except Exception:
            return value


def decrypt_payload(data: Dict) -> Dict:
    decrypter = Decrypter()
    return {key: decrypter.decode(value) for key, value in data.items()}
