import hmac
import os
import json
from typing import Dict
import hashlib
import sys


class Signer:
    secret_key = os.environ.get("SECRET_KEY")
    if secret_key is None:
        sys.exit(
            """
            Error: The environment variable SECRET_KEY is required.
            Try :
                docker run -e SECRET_KEY=your_secret_key
            or
                export SECRET_KEY=your_secret_key
            """
        )

    hash_algo = hashlib.sha256

    def sign(self, payload: Dict) -> str:
        payload = dict(sorted(payload.items()))

        key_bytes = bytes(self.secret_key, "utf-8")
        message = bytes(json.dumps(payload), "utf-8")

        signature = hmac.new(key_bytes, message, self.hash_algo).hexdigest()

        return signature


def sign_payload(payload: Dict) -> Dict:
    signer = Signer()
    return {"signature": signer.sign(payload)}
