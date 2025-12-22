# Agent Compiler (Prototype)

Design-time governance for AI agents.

This project demonstrates a **compile-only** system for AI agents:
Intent → Plan → Diff → Publish

It does NOT execute agents. It generates **reviewable artifacts** that can later be consumed by runtimes like LangGraph.

## Philosophy

This project focuses on **design-time decisions**, not runtime autonomy.

Agents should not decide:
- what they are allowed to do
- which tools they can access
- when humans must approve actions

Those decisions belong in a compile-time layer.

This repository explores what that layer could look like.


## Run locally
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://localhost:8000/health

## Roadmap (early ideas)

- [ ] Rich intent schema (capabilities, constraints, risk tiers)
- [ ] Deterministic topology selection rules
- [ ] Capability diffing across versions
- [ ] Export adapters for agent runtimes (e.g. LangGraph)
- [ ] Design-time approval workflows

