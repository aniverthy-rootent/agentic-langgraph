# agentic-langgraph

**11 multi-agent applications built with LangGraph.**  
Theme: _Business & operations workflows as stateful graphs_

[LangGraph](https://github.com/langchain-ai/langgraph) models agent teams as stateful graphs: nodes are agents, edges are hand-offs, and a shared state carries every agent's output.

## Quick start (no API key needed)

```bash
pip install -r requirements.txt
python run_all.py                       # run all 11 apps
python -m apps.app01_order_fulfillment   # run a single app
pytest -q                               # smoke tests for every app
```

Every app runs against a deterministic offline model (`common/offline_llm.py`) so you can watch the orchestration work without credentials.

## How it works

`runtime.py` compiles each app's agent list into a `StateGraph`. Sequential apps become a chain; fan-out apps add parallel branches and a join edge before the final merger agent.

## Using a real model

In `runtime.py`, replace `call_llm` with a LangChain chat model, e.g.

```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini")
def call_llm(system, user):
    return llm.invoke([("system", system), ("human", user)]).content
```

## Applications

| # | Application | Agents | Roles |
|---|---|---|---|
| 1 | Order Fulfillment Graph | 5 | Order Validator, Inventory Allocator, Fraud Screener, Shipping Planner, Notification Agent |
| 2 | Invoice Processing | 5 | OCR Extractor, PO Matcher, Tax Checker, Approval Router, Ledger Poster |
| 3 | Loan Underwriting | 6 | Applicant Profiler, Credit Analyst, Cash Flow Analyst, Collateral Appraiser, Risk Officer, Decision Writer |
| 4 | Insurance Claims Adjudication | 5 | Claim Intake, Policy Checker, Damage Estimator, Fraud Detector, Settlement Negotiator |
| 5 | Supply Chain Disruption Response | 5 | Disruption Monitor, Supplier Finder, Cost Modeler, Production Planner, Customer Communicator |
| 6 | Meeting Follow-up Automation | 5 | Transcript Cleaner, Decision Extractor, Action Item Tracker, Risk Spotter, Summary Writer |
| 7 | Expense Audit | 5 | Receipt Reader, Policy Auditor, Duplicate Detector, Anomaly Analyst, Audit Reporter |
| 8 | B2B Customer Onboarding | 6 | Kickoff Planner, Data Migrator, Integration Engineer, Training Designer, Success Manager, Go-Live Reviewer |
| 9 | Warehouse Slotting Optimizer | 5 | Demand Profiler, Affinity Analyst, Layout Planner, Labor Estimator, Change Manager |
| 10 | Procurement RFP Evaluation | 5 | Requirement Extractor, Proposal Scorer, Cost Analyst, Risk Assessor, Recommendation Writer |
| 11 | Workforce Scheduling | 5 | Demand Forecaster, Availability Collector, Schedule Builder, Compliance Checker, Fairness Auditor |

Full per-agent instructions are in [AGENTS.md](AGENTS.md).

Each app uses one of two data-flow patterns (see `common/flow.py`):
`sequential` (each agent builds on the previous) or `fanout` (a planner, parallel specialists, then a merger).

## License

MIT
