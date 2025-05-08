from fastapi import FastAPI
from src.endpoint.encrypt import router as encrypt_router
from src.endpoint.decrypt import router as decrypt_router

from src.endpoint.sign import router as sign_router
from src.endpoint.verify import router as verify_router


app = FastAPI()

app.include_router(encrypt_router)
app.include_router(decrypt_router)

app.include_router(sign_router)
app.include_router(verify_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
