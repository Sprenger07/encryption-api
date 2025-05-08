from typing import Dict


from fastapi import APIRouter, HTTPException
from services.encryption_service import encrypt_payload

router = APIRouter()


@router.post("/encrypt")
def post_encrypt(payload: Dict | None = None) -> Dict:
    if payload is None:
        raise HTTPException(status_code=400, detail="Invalid payload")
    return encrypt_payload(payload)
