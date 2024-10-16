from fastapi import FastAPI
from pydantic import BaseModel

from audio_service import play_audio
from camera_service import take_photo

app = FastAPI()

@app.get("/callback")
def read_root():
    take_photo()
    return {"Hello": "World"}

@app.get("/play-audio")
def play():
    play_audio()
    return "done"

"""
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
class Event(BaseModel):
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

