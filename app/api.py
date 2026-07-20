from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import Agent

app = FastAPI(
    title="Smart Agent",
    version="1.3"
)

agent = Agent()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    model: str
    messages: list[Message]


@app.get("/")
def root():
    return {
        "service": "Smart Agent",
        "version": "1.3"
    }


@app.get("/v1/models")
def models():

    return {
        "object": "list",
        "data": [
            {
                "id": "smart-agent",
                "object": "model",
                "owned_by": "local"
            }
        ]
    }


@app.post("/v1/chat/completions")
def chat(request: ChatRequest):

    question = request.messages[-1].content

    answer = agent.ask(question)

    return {
        "id": "chatcmpl-local",
        "object": "chat.completion",
        "model": request.model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": answer
                },
                "finish_reason": "stop"
            }
        ]
    }