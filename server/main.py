from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json


app= FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Word(BaseModel):
    title: str 
    content : str

words = [
    {
        "id": 1,
        "title": "Ambiguous",  
        "meaning":"Open to multiple interpretations; having a double meaning",
    },
    {
        "id":2,
        "title": "Conundrum",
        "meaning": "A confusing and difficult problem or question",
    },
    {
        "id":3,
        "title": "Disparate",
        "meaning": "Essentially different in kind; not allowing comparison",
    },
]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    global words
    while True:
        data = await websocket.receive_json()
        if (data["type"]=="get_words"):
            await websocket.send_json(words)
        if (data["type"]=="delete_word"):
            words = [word for word in words if word["title"] != data["value"]]
            await websocket.send_json(words)
        if (data["type"] == "add_word"):
            words.append(json.loads( data["value"]))
            await websocket.send_json(words)

