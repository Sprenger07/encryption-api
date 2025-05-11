import base64
import json
from typing import Dict


class Encrypter:
    def encoding_algo(self, formated_value) -> str:
        return base64.b64encode(bytes(formated_value, "utf-8")).decode("utf-8")

    def encode(self, value) -> str:
        if isinstance(value, (dict, list)):
            formated_value = json.dumps(value, separators=(",", ":"))
        else:
            formated_value = str(value)
        return self.encoding_algo(formated_value)


def encrypt_payload(data: Dict) -> Dict:
    encrypter = Encrypter()
    return {key: encrypter.encode(value) for key, value in data.items()}
