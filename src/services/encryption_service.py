import base64
import json
from typing import Dict


class Encoder:
    def encode(self, value) -> str:
        if isinstance(value, (dict, list)):
            format_value = json.dumps(value, separators=(",", ":"))
        else:
            format_value = str(value)
        return base64.b64encode(format_value.encode("utf-8")).decode("utf-8")


def encrypt_payload(data: Dict) -> Dict:
    encoder = Encoder()
    return {key: encoder.encode(value) for key, value in data.items()}
