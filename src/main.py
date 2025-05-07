from typing import Dict

import base64
import json

from fastapi import FastAPI, HTTPException

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
