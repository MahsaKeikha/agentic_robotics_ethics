from orchestration.orchestrator import run

context = {
    "objective": "review the ethics of a proposed service robot deployment",
    "stakeholder_impact_reviewed": True,
    "human_agency_reviewed": True,
    "fairness_reviewed": True,
    "transparency_reviewed": True,
    "privacy_reviewed": True,
    "misuse_reviewed": True,
    "accountability_reviewed": True,
    "contestability_reviewed": True,
    "governance_reviewed": True,
    "human_approval": True,
}

print(run(context))
