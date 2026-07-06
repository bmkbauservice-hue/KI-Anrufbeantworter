from fastapi import FastAPI
from pydantic import BaseModel

from brain.brain import AIBrain


class BrainRequest(BaseModel):
    text: str


app = FastAPI(
    title="AI CallFlow API",
    version="0.1.0"
)

brain = AIBrain()


@app.get("/")
def root():
    return {
        "message": "AI CallFlow läuft 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "online"
    }


@app.post("/brain")
def process_text(request: BrainRequest):
    return brain.process(request.text)