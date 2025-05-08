from fastapi import APIRouter, HTTPException, status
import hmac
import os
import hashlib
from typing import Dict
import json

router = APIRouter()


@router.post("/verify", status_code=status.HTTP_204_NO_CONTENT)
def post_verify(payload: Dict | None = None) -> None:
    if payload is None:
        raise HTTPException(status_code=400, detail="Missing payload")

    if payload.get("signature") is None:
        raise HTTPException(status_code=400, detail="Missing signature")

    if payload.get("data") is None:
        raise HTTPException(status_code=400, detail="Missing data")

    payload = dict(sorted(payload.items()))

    secret_key = os.environ.get("SECRET_KEY")

    signature = hmac.new(
        bytes(secret_key, "utf-8"), bytes(json.dumps(payload), "utf-8"), hashlib.sha256
    ).hexdigest()

    if signature == payload.get("signature"):
        return
    else:
        HTTPException(status_code=400, detail="Invalid signature")
