from fastapi import FastAPI
from app.mood_engine import MoodEngine

app = FastAPI(title="Minimal Robot Mood Engine")

engine = MoodEngine()


@app.post("/event/{event_name}")
def process_event(event_name: str):
    engine.apply_event(event_name)
    return {"status": "processed", "event": event_name}


@app.get("/state")
def get_state():
    return engine.get_state()

