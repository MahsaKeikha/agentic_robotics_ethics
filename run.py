from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "robotics ethics review",
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

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
