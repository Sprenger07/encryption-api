from typing import Dict

import base64
import hashlib
import json
import hmac
import os

from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/encrypt")
def post_encrypt(payload: Dict | None = None) -> Dict:
    if payload is None:
        raise HTTPException(status_code=400, detail="Invalid payload")

    encrypted_data = {}
    for key, value in payload.items():
        if type(value) is dict:
            encoded_value = base64.b64encode(
                bytes(json.dumps(value, separators=(",", ":")), "utf-8")
            )
        else:
            encoded_value = base64.b64encode(bytes(str(value), "utf-8"))
        encrypted_data.update({key: encoded_value})

    return encrypted_data


@app.post("/decrypt")
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


@app.post("/sign")
def post_sign(payload: Dict | None = None) -> Dict:
    if payload is None:
        raise HTTPException(status_code=400, detail="Invalid payload")

    payload = dict(sorted(payload.items()))

    secret_key = os.environ.get("SECRET_KEY")

    signature = hmac.new(
        bytes(secret_key, "utf-8"), bytes(json.dumps(payload), "utf-8"), hashlib.sha256
    ).hexdigest()

    return {"signature": signature}


@app.post("/verify", status_code=status.HTTP_204_NO_CONTENT)
def verify_sign(payload: Dict | None = None) -> None:
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
