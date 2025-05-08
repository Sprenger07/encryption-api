from fastapi import APIRouter, HTTPException
from typing import Dict
from services.sign_service import sign_payload

router = APIRouter()


@router.post("/sign")
def post_sign(payload: Dict | None = None) -> Dict:
    if payload is None:
        raise HTTPException(status_code=400, detail="Invalid payload")
    return sign_payload(payload)
