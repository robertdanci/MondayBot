import logging
from typing import Dict, Any

from fastapi import FastAPI
from pydantic import BaseModel

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
    print(body)
    if body.challenge:
        print("handling challenge scenario")
        return {"challenge": body.challenge}
    print("handling event")
    return "ok"


@app.post("/echo")
def play(payload: Dict[Any, Any]):
    logger.info(payload)
    return payload