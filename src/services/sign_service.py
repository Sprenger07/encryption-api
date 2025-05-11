import hmac
import os
import json
from typing import Dict
import hashlib
import sys


class Signer:
    secret_hashing_key = os.environ.get("SECRET_HASHING_KEY")
    if secret_hashing_key is None:
        sys.exit(
            """
            Error: The environment variable SECRET_KEY is required.
            Try :
                docker run -e SECRET_HASHING_KEY=your_secret_key
            or
                export SECRET_HASHING_KEY=your_secret_key
            """
        )

    def signing_algo(self):
        return hashlib.sha256

    def sign(self, payload: Dict) -> str:
        payload = dict(sorted(payload.items()))

        key_bytes = bytes(self.secret_hashing_key, "utf-8")
        message = bytes(json.dumps(payload), "utf-8")

        signature = hmac.new(key_bytes, message, self.signing_algo()).hexdigest()

        return signature


def sign_payload(payload: Dict) -> Dict:
    signer = Signer()
    return {"signature": signer.sign(payload)}
