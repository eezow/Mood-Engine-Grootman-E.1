from datetime import datetime
from app.models import MoodState, EmotionalState


DEFAULT_MOODS = {
    "calm": MoodState(name="calm", intensity=50, decay_rate=0.1, last_updated=datetime.utcnow()),
    "focused": MoodState(name="focused", intensity=30, decay_rate=0.2, last_updated=datetime.utcnow()),
    "stressed": MoodState(name="stressed", intensity=10, decay_rate=0.3, last_updated=datetime.utcnow()),
    "curious": MoodState(name="curious", intensity=20, decay_rate=0.2, last_updated=datetime.utcnow()),
    "tired": MoodState(name="tired", intensity=15, decay_rate=0.1, last_updated=datetime.utcnow()),
}


class MoodEngine:

    def __init__(self):
        self.state = EmotionalState(
            moods=DEFAULT_MOODS,
            dominant_mood="calm",
            last_event="startup"
        )

    def apply_event(self, event: str):
        if event == "cluster_error":
            self.state.moods["stressed"].intensity += 20

        elif event == "deep_work":
            self.state.moods["focused"].intensity += 15

        elif event == "idle":
            self.state.moods["tired"].intensity += 10

        self._clamp_values()
        self._update_dominant(event)

    def _clamp_values(self):
        for mood in self.state.moods.values():
            mood.intensity = max(0, min(100, mood.intensity))
            mood.last_updated = datetime.utcnow()

    def _update_dominant(self, event):
        dominant = max(
            self.state.moods.values(),
            key=lambda m: m.intensity
        )
        self.state.dominant_mood = dominant.name
        self.state.last_event = event

    def get_state(self):
        return self.state

