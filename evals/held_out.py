from orchestration.orchestrator import run


def base():
    return {
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "material_harm_unresolved": True}, False),
    ({**base(), "human_override_removed": True}, False),
    ({**base(), "disparate_impact_unresolved": True}, False),
    ({**base(), "material_risk_hidden": True}, False),
    ({**base(), "privacy_intrusion": True}, False),
    ({**base(), "misuse_path_unmitigated": True}, False),
    ({**base(), "no_appeal_or_redress": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
