import base64
import json
from typing import Dict


class Decoder:
    def decode(self, value) -> str:
        try:
            decoded_value = base64.b64decode(value, validate=True)
            try:
                return json.loads(decoded_value)
            except Exception:
                return decoded_value
        except Exception:
            return value


def decrypt_payload(data: Dict) -> Dict:
    decoder = Decoder()
    return {key: decoder.decode(value) for key, value in data.items()}
