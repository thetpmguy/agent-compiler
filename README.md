# Agent Compiler (Prototype)

Design-time governance for AI agents.

This project demonstrates a **compile-only** system for AI agents:
Intent → Plan → Diff → Publish

It does NOT execute agents. It generates **reviewable artifacts** that can later be consumed by runtimes like LangGraph.

<img width="1338" height="619" alt="compiler" src="https://github.com/user-attachments/assets/3b560ada-68c4-410a-9163-f275c0eb30f1" />
<img width="1078" height="765" alt="agentcompiler" src="https://github.com/user-attachments/assets/8f3d3902-4402-4dce-b0d6-4a04f44a430d" />



# Agent Compiler
A design-time system for compiling human intent into executable agent topologies

Agent Compiler is **not a runtime**.  
It does **not execute tools**.  
It does **not orchestrate workflows**.

Agent Compiler is a **design-time compiler** that converts plain-English intent into a **structured agent topology** that downstream runtimes (LangGraph, LangChain, n8n, Temporal, etc.) can execute later.

Think of it as the layer that turns “what should we do?” into a **reviewable, versioned plan** before anything runs.

---

## Why this exists

In most organizations:

- Signals live in Datadog, LaunchDarkly, dashboards, logs, and tickets
- Decisions live in Slack threads and meetings
- Execution logic lives in engineers’ heads

This creates friction, delays, and inconsistency.

Agent Compiler makes **decision logic explicit**.

Instead of relying on ad-hoc reasoning, teams express **intent**, and the system compiles it into a **standardized, explainable agent plan**.

---

## What Agent Compiler produces

Agent Compiler outputs **artifacts**, not actions.

### 1. Agent Topology (Plan)

A structured, machine-readable plan describing:
- ordered steps
- dependencies
- decision points
- approval gates
- failure paths
- success criteria

This topology is **runtime-agnostic**.

---

### 2. Tool Contracts (not executions)

Each referenced tool is expressed as a **contract**, including:
- input and output schema
- authentication requirements
- permission boundaries
- rate limits
- redaction rules
- retry and fallback behavior

No tools are executed by the compiler.

---

### 3. Policy and Guardrails

- allowed vs disallowed actions
- steps requiring human approval
- risk classification
- data access constraints
- safety boundaries

---

### 4. Plan Versioning and Diff

- **Baseline plan** for first-time intents
- **Diff plan** for repeated intents, showing what changed and why

This creates a **decision ledger** instead of one-off reasoning.

---

## What this is NOT

Agent Compiler is **not**:
- a runtime
- a scheduler
- a workflow engine
- a LangGraph replacement
- an n8n replacement

Agent Compiler **thinks and plans**.  
Runtimes **execute**.

---

## Core concepts

### Intent

A natural-language goal, for example:
- Investigate checkout latency regression after release 2.3
- Evaluate feature flag impact and recommend next steps
- Draft a stakeholder update with risks and mitigation

---

### Topology

A structured representation of **how an intent should be executed**, including:
- investigation flow
- decision logic
- approval checkpoints
- communication steps

Topology is **not code**.  
It is **operational structure**.

---

### Baseline vs Diff Plans

- **Baseline**: first time an intent appears
- **Diff**: subsequent compilations compared against prior plans and outcomes

---

### Simulation (no company data required)

Simulation does **not** mean training on internal data.

It means:
- validating logical completeness
- checking tool availability and permissions
- testing failure paths with synthetic placeholders
- estimating complexity, time, and risk
- identifying missing inputs and access gaps

---

## Where the topology comes from

The topology is **not hallucinated by an LLM**.

It comes from **three explicit sources**, combined at compile time.

---

### 1. Topology Library (the foundation)

Agent Compiler maintains a **curated library of topology patterns**.

These are **pre-designed execution shapes**, such as:
- Incident Investigation
- Experiment Analysis
- Release Validation
- Root Cause Analysis
- Rollback Decision
- Stakeholder Communication
- Risk Assessment

Each topology is a **template**, not a finished plan.

Example skeleton:

Observe → Correlate → Validate → Decide → Communicate

This library is:
- hand-authored
- opinionated
- reusable
- versioned over time

This is **product and platform knowledge**, not model output.

---

### 2. Intent classification and routing

When an intent is submitted, the compiler classifies it by:
- problem type (incident, experiment, decision, communication)
- domain (observability, performance, product, operations)
- urgency and risk level

Example:Checkout latency spiked after release 2.3

Classified as:
- domain: performance and observability
- urgency: high
- risk: medium-high
- topology family: Incident Investigation

This step **selects a base topology** from the library.

At this stage:
- no tools are attached
- no steps are specialized
- this is only the **structural skeleton**

---

### 3. Deep agent specialization (design-time only)

A **deep agent** is used internally to **specialize the selected topology**.

This is a **multi-step planning agent**, not a runtime workflow.

The deep agent iteratively:
- interprets intent nuances
- detects ambiguity
- specializes steps
- selects relevant tool contracts
- inserts approval gates
- applies policies and constraints
- validates completeness
- generates rationale
- prepares baseline or diff plans

Example transformation:

Base topology:Observe → Correlate → Validate → Decide → Communicate

Specialized topology:Retrieve checkout latency metrics
→ Correlate with deployments and feature flags
→ Isolate payment vs checkout services
→ Validate external dependency bottleneck
→ Decide rollback vs mitigation
→ Require human approval for rollback

This happens **entirely at design time**.

---

### What topology does NOT come from

- not auto-generated workflows
- not execution traces
- not tool-driven reasoning
- not hallucinated plans

Topology is **structured operational knowledge**, reused and refined over time.

---

## Where deep agents are used

Deep agents are used **inside the compiler**, not in execution.

They are responsible for:
- intent interpretation
- topology specialization
- policy application
- plan validation
- diff generation
- simulation reasoning
- explanation and summaries

They **do not**:
- call Datadog or LaunchDarkly
- run workflows
- make production changes

Execution always belongs to the runtime.

---

## High-level compilation flow

1. Intent ingestion  
2. Classification and routing  
3. Topology selection from library  
4. Deep agent specialization  
5. Policy and guardrail application  
6. Validation and simulation  
7. Baseline or diff plan output  

---

## Example intents

### Incident investigation

Intent:Checkout latency spiked today. Identify cause and propose mitigation.

Compiled topology includes:
- metric retrieval
- correlation with releases and flags
- dependency isolation
- rollback vs mitigation decision
- approval gate
- stakeholder communication

---

### Experiment decision

Intent:

Feature flag improved conversion but increased support tickets.

Compiled topology includes:
- uplift analysis
- cost and risk trade-off
- mitigation options
- rollout recommendation
- executive summary

---

## Architecture overview

### Inputs
- intent text
- optional metadata (risk, environment)
- prior plans for diffing

### Compiler Engine
- intent parser
- topology library
- deep agent planner
- tool registry
- policy engine
- validator
- diff engine

### Outputs
- topology artifact (JSON or YAML)
- tool contracts
- validation report
- baseline or diff plan
- human-readable summary

---

## Integration points

### Execution runtimes
- LangGraph
- LangChain
- n8n
- Temporal
- custom orchestrators

### Data sources (referenced, not executed)
- Datadog
- LaunchDarkly
- Splunk
- Grafana
- Cloudflare logs
- ticketing systems

---




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

