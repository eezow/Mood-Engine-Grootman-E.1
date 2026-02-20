from pydantic import BaseModel
from datetime import datetime
from typing import Dict


class MoodState(BaseModel):
    name: str
    intensity: int
    decay_rate: float
    last_updated: datetime


class EmotionalState(BaseModel):
    moods: Dict[str, MoodState]
    dominant_mood: str
    last_event: str

