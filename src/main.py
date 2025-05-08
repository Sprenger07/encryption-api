from fastapi import FastAPI
from endpoint.encrypt import router as encrypt_router
from endpoint.decrypt import router as decrypt_router

from endpoint.sign import router as sign_router
from endpoint.verify import router as verify_router


app = FastAPI()

app.include_router(encrypt_router)
app.include_router(decrypt_router)

app.include_router(sign_router)
app.include_router(verify_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
