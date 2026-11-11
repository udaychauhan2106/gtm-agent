# GTM Agent — Lead Research Workflow

An early-stage Python project exploring how a stateful LangGraph workflow can qualify and research B2B leads using typed domain models and tools.

> **Status: Work in progress.** The current repository is a prototype / learning implementation, not a production-ready sales automation system.

## Current scope

- Pydantic domain models for companies, contacts, leads, research reports, sources and signals.
- Typed LangGraph state.
- A basic graph with lead loading, qualification and research stages.
- Mock company data and a company lookup tool.
- Pytest foundation for domain-model tests.

## Current workflow

```text
Lead
  |
  v
Load company and contact
  |
  v
Qualify lead
  |
  +-- Not qualified --> End
  |
  v
Research lead
  |
  v
Research report
```

The current qualification logic is intentionally simple and uses the presence of a company website as an initial signal. Research currently creates a basic report from mock company data. It does not yet perform comprehensive external research or autonomous outreach.

## Technology

- Python 3.12+
- LangGraph
- LangChain tools
- Pydantic
- uv
- pytest

## Project layout

- `src/gtm_agent/domain/models/` — typed business and research models.
- `src/gtm_agent/graphs/` — graph state and workflow.
- `src/gtm_agent/tools/` — callable tools.
- `src/gtm_agent/data/` — mock data.
- `src/gtm_agent/experiments/` — tool-calling experiments.
- `tests/` — model tests.

## Setup

Install [uv](https://docs.astral.sh/uv/) and run:

```bash
uv sync
uv run pytest
```

The graph prototype can be explored from `src/gtm_agent/graphs/basic_graph.py`. It currently contains a small local invocation example; the workflow is still being separated from experimental/demo execution.

## Planned engineering work

- Replace mock-only qualification with evidence-backed research.
- Track source provenance and timestamps for every research claim.
- Add explicit qualification criteria and explainable outcomes.
- Persist lead and research state.
- Add retry, timeout and failure handling for external tools.
- Build evaluation cases for research accuracy and qualification quality.
- Add human approval before any outbound action.
