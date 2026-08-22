# F80 | Agentic Robotics Ethics | L3 Gold Standard | v1.0

A governed multi-agent reference implementation for robotics ethics analysis, stakeholder impact, human agency, fairness, transparency, governance, and accountability.

## Six-agent architecture

- [Stakeholder Impact](AGENTS/stakeholder_impact_agent.py)
- [Human Agency](AGENTS/human_agency_agent.py)
- [Fairness Review](AGENTS/fairness_review_agent.py)
- [Transparency](AGENTS/transparency_agent.py)
- [Governance](AGENTS/governance_agent.py)
- [Accountability](AGENTS/accountability_agent.py)

Tools and skills are exposed in `TOOLS/` and `SKILLS/`, with orchestration, memory, state, schemas, prompts, configuration, safety, observability, evals, benchmarks, examples, tests, docs, and CI.

## Gold-standard governance

F80 is fail closed. Recommendation release requires stakeholder-impact, human-agency, fairness, transparency, privacy, misuse, accountability, contestability, governance, and qualified-human reviews.

Release is blocked for unresolved material harm, loss of meaningful human override, unresolved disparate impact, hidden material risk, privacy intrusion, unmitigated misuse paths, accountability gaps, or missing appeal and redress mechanisms.

The reference system supports nonbinding ethics analysis only. It has no authority to control robots, make binding policy decisions, remove human override, hide material risk, autonomously enforce policy, or use covert persuasion.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

The verification layer includes eight direct governance tests and a 10-scenario held-out robotics-ethics suite.
