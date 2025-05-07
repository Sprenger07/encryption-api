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
                bytes(
                    "{" + ", ".join(f'"{k}":"{v}"' for k, v in value.items()) + "}",
                    "utf-8",
                )
            )
        else:
            encoded_value = base64.b64encode(bytes(str(value), "utf-8"))
        encrypted_data.update({key: encoded_value})

    return encrypted_data


