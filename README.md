# Mood-Engine

Well Look , this is hobby from from a Nerdy kid (ME) in south africa , im obsessed about Robotics and it doesnt Seem like South Africa is in to that kind of thing so i want to be one of the first ones to build a responsive and some what useful robot .. so this is about building a Mood Responsive Robot , well give it a name later..for now lets assume its called Grootman E.1.

Tools
Python 3.11+

FastAPI

Redis

Uvicorn

Docker

Minimal Robot – Phase 1: Mood Engine Core

Emotional State Schema

Each mood has:
name
intensity (0–100)
decay_rate (per minute)
last_updated

We track 5 moods:
calm
focused
stressed
curious
tired

We also define:
dominant_mood
last_event

Folder structure
minimal-robot/
│
├── app/
│   ├── main.py
│   ├── mood_engine.py
│   ├── models.py
│   └── config.py
│
├── requirements.txt
├── Dockerfile
└── README.md


To keep it minimal on requirements ill only add ;
fastapi
uvicorn
redis
pydantic
