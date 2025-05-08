from fastapi import APIRouter, HTTPException
import hmac
import os
import json
from typing import Dict
import hashlib


router = APIRouter()


@router.post("/sign")
def post_sign(payload: Dict | None = None) -> Dict:
    if payload is None:
        raise HTTPException(status_code=400, detail="Invalid payload")

    payload = dict(sorted(payload.items()))

    secret_key = os.environ.get("SECRET_KEY")

    signature = hmac.new(
        bytes(secret_key, "utf-8"), bytes(json.dumps(payload), "utf-8"), hashlib.sha256
    ).hexdigest()

    return {"signature": signature}
