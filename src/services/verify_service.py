from src.services.sign_service import Signer
from typing import Dict
import hmac


class Verifier:
    signer = Signer()

    def verify(self, data: Dict, signature: str) -> bool:
        expected_signature = self.signer.sign(data)
        return hmac.compare_digest(expected_signature, signature)


def verify_payload(data: Dict, signature: str) -> bool:
    verifier = Verifier()
    return verifier.verify(data, signature)
