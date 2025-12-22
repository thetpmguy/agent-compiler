# Agent Compiler (Prototype)

Design-time governance for AI agents.

This project demonstrates a **compile-only** system for AI agents:
Intent → Plan → Diff → Publish

It does NOT execute agents. It generates **reviewable artifacts** that can later be consumed by runtimes like LangGraph.

## Run locally
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://localhost:8000/health
