import logging
import os
from os import environ
from typing import Dict, Any

from fastapi import FastAPI
from pydantic import BaseModel

from app.audio_service import play_audio
from app.camera_service import take_photo

logger = logging.getLogger(__name__)

app = FastAPI()

import requests
import json

headers = {
        'Authorization': os.environ.get("ACCESS_TOKEN"),
        'Content-Type': 'application/json',
        'API-version': '2023-10'
    }

def update_monday_pulse(pulse_id: int):
    logger.info(f"updating pulse {pulse_id}")

    query = "mutation {create_update (item_id:" + str(pulse_id) + ", body: \"Incredible! Checkout this image of the moment!!\") {id}}"
    payload = json.dumps({
        "query": query
    })
    response = requests.request("POST", "https://api.monday.com/v2", headers=headers, data=payload)

    logger.info(response.text)
    return response.json()["data"]["create_update"]["id"]

def upload_file_to_monday_update(image_path: str):
    payload = {'query': 'mutation ($file: File!) {add_file_to_update(file: $file, update_id: 3542401699) {id}}'}
    files = [('image', ('picture.png', open(image_path, 'rb'), 'image/png'))]
    response = requests.request("POST", "https://api.monday.com/v2/file", headers=headers, data=payload, files=files)
    logger.info(response.text)

@app.post("/take-photo")
def read_root():
    take_photo()
    return "done"

@app.post("/play-audio")
def play():
    play_audio()
    return "done"

class Event(BaseModel):
    """
    Mirrors the monday webhook event payload for boards
    {
      app: 'monday',
      type: 'update_column_value',
      triggerTime: '2024-10-16T11:44:03.781Z',
      subscriptionId: 420586429,
      userId: 43066799,
      originalTriggerUuid: null,
      boardId: 7410328198,
      groupId: 'group_title',
      pulseId: 7410328521,
      pulseName: 'Item 5',
      columnId: 'status',
      columnType: 'color',
      columnTitle: 'Status',
      value: {
        label: { index: 1, text: 'Done', style: [Object], is_done: true },
        post_id: null
      },
    """
    app: str
    type: str
    triggerTime: str
    subscriptionId: int
    userId: int
    boardId: int
    groupId: str
    pulseId: int
    pulseName: str
    columnId: str
    columnType: str
    columnTitle: str
    # we don't need the value object because the automation is setup to only trigger when status changes to DONE

class WebHookBody(BaseModel):
    event: Event | None = None
    challenge: str | None = None

@app.post("/webhook")
def webhook_handler(body: WebHookBody):
    if body.challenge:
        logging.info("handling challenge scenario")
        return {"challenge": body.challenge}
    update_id = update_monday_pulse(body.event.pulseId)
    # image_path = take_photo()
    # upload_file_to_monday_update()
    return "ok"


@app.post("/echo")
def play(payload: Dict[Any, Any]):
    logger.info(payload)
    return payload