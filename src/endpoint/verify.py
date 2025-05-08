from fastapi import APIRouter, HTTPException, status
from typing import Dict
from services.verify_service import verify_payload

router = APIRouter()


@router.post("/verify", status_code=status.HTTP_204_NO_CONTENT)
def post_verify(payload: Dict | None = None) -> None:
    if payload is None:
        raise HTTPException(status_code=400, detail="Missing payload")

    if payload.get("signature") is None:
        raise HTTPException(status_code=400, detail="Missing signature")

    if payload.get("data") is None:
        raise HTTPException(status_code=400, detail="Missing data")

    data = payload.get("data")
    signature = payload.get("signature")

    if not verify_payload(data, signature):
        HTTPException(status_code=400, detail="Invalid signature")
