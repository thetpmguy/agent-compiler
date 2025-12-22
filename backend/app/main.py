from fastapi import FastAPI
import yaml

app = FastAPI(title="Agent Compiler Prototype")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/compile")
def compile_intent(intent_yaml: str):
    intent = yaml.safe_load(intent_yaml)
    plan = {
        "goal": intent.get("goal"),
        "steps": ["retrieve", "draft", "review", "publish"],
        "requires_approval": True
    }
    return {
        "intent": intent,
        "plan": plan
    }
