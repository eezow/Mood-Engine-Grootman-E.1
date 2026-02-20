# Grootman E.1

Well Look, this is a Dream Hobby Project from from a Nerdy kid (ME) in south africa, im obsessed about Robotics and it doesnt Seem like South Africa is in to that kind of thing so i want to be one of the first ones to build a responsive and some what useful robot .. so this is about building a Mood Responsive Robot, well give it a name later..for now lets assume its called Grootman E.1. 

Created and maintained Caleb Lindani Mathebula

FEEL FREE TO CONTRIBUTE BUT ALWAYS CREDIT THE ORIGINAL CREATOR: CALEB LINDANI MATHEBULA ( ME ! ) - LET'S  BUILD!

This Project will be built in 3  phases.

Phase 1 – The Brain

Phase 2 – Hardware Shell

Phase 3 – Mood Detection

## Features
- Event-based mood transitions
- Time-based decay
- Dominant mood detection
- Dockerized deployment


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

the get state
 
curl http://127.0.0.1:8000/state

<img width="1094" height="151" alt="image" src="https://github.com/user-attachments/assets/65182774-d7e4-4072-b517-63c1c574f282" />


Next STEP is to package Grootman into Docker

sudo docker build -t grootman_e:1 -f grootman_e.1 .

<img width="680" height="258" alt="image" src="https://github.com/user-attachments/assets/79c44d00-4d7d-4725-8cf2-4b88197f51f8" />


<img width="931" height="460" alt="image" src="https://github.com/user-attachments/assets/37f9f9e5-04ba-489e-a227-42f89ac5bbb0" />

run  : sudo docker run -p 8000:8000 grootman_e:1

<img width="716" height="214" alt="image" src="https://github.com/user-attachments/assets/aa905c09-d349-4bbe-a58c-5249d1303328" />




Up till now - Grootman works but if the container shutsdown - the mood is reset ...well thats not realistic so how can we persist their Mood ??


We add: Redis persistence So mood survives container restart ? HOW ?

Store mood state in Redis

So container restarts don’t reset personality

And multiple instances can share the same emotional brain



