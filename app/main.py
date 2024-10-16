from fastapi import FastAPI

from app.audio_service import play_audio
from app.camera_service import take_photo

app = FastAPI()

@app.get("/callback")
def read_root():
    take_photo()
    return {"Hello": "World"}

@app.get("/play-audio")
def play():
    play_audio()
    return "done"

