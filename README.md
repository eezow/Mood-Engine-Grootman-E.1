# Mood-Engine

Well Look , this is hobby from from a Nerdy kid (ME) in south africa , im obsessed about Robotics and it doesnt Seem like South Africa is in to that kind of thing so i want to be one of the first ones to build a responsive and some what useful robot .. so this is about building a Mood Responsive Robot , well give it a name later..for now lets assume its called Grootman E.1. 
This Project will be built in 3  phases.

Phase 1 – The Brain
Phase 2 – Hardware Shell
Phase 3 – Mood Detection


Tools

Python 3.11+

FastAPI

Redis

Uvicorn

Docker

Minimal Robot – Phase 1: Mood Engine Core - the Goal for this phase is to get to A distributed emotional state system running on K8s.

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



Environment Setup

python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn redis pydantic

If pip is missing:

python3 -m ensurepip --upgrade

We use python3 -m uvicorn to avoid PATH issues.

🚀 What I Expect Next
When it runs successfully you should see:
Uvicorn running on http://127.0.0.1:8000

<img width="805" height="190" alt="image" src="https://github.com/user-attachments/assets/52a9b7d5-52a9-478a-aead-2be3ef2ea2d5" />

Then test:
curl -X POST http://127.0.0.1:8000/event/cluster_error
curl http://127.0.0.1:8000/state

<img width="1094" height="151" alt="image" src="https://github.com/user-attachments/assets/65182774-d7e4-4072-b517-63c1c574f282" />


