from typing import Dict

from fastapi import APIRouter, HTTPException
from src.services.decryption_service import decrypt_payload

router = APIRouter()


@router.post("/decrypt")
def post_decrypt(payload: Dict | None = None) -> Dict:
    if payload is None:
        raise HTTPException(status_code=400, detail="Invalid payload")

    return decrypt_payload(payload)
