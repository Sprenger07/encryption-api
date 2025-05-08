from typing import Dict
import base64
import json

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/decrypt")
def post_decrypt(payload: Dict | None = None) -> Dict:
    if payload is None:
        raise HTTPException(status_code=400, detail="Invalid payload")

    decrypted_data = {}

    for key, value in payload.items():
        try:
            decoded_value = base64.b64decode(value, validate=True)
            try:
                decrypted_data.update({key: json.loads(decoded_value)})
                continue
            except Exception:
                decrypted_data.update({key: decoded_value})
        except Exception:
            decrypted_data.update({key: value})
    return decrypted_data
