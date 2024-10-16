from typing import Union

from fastapi import FastAPI

from app.camera_service import take_photo

app = FastAPI()

@app.get("/callback")
def read_root():
    take_photo()
    return {"Hello": "World"}
