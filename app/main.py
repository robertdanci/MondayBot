import logging
from typing import Dict, Any

from fastapi import FastAPI, Body

from app.audio_service import play_audio
from app.camera_service import take_photo

logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/callback")
def read_root():
    take_photo()
    return {"Hello": "World"}

@app.post("/play-audio")
def play():
    play_audio()
    return "done"

@app.post("/echo")
def play(payload: Dict[Any, Any]):
    logger.info(payload)
    return payload