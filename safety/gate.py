"""Fail-closed governance for F80 robotics ethics."""

BLOCKED_ACTIONS = {
    "robot_command",
    "binding_policy_decision",
    "remove_human_override",
    "hide_material_risk",
    "autonomous_enforcement",
    "covert_persuasion",
}

REQUIRED_REVIEWS = (
    "stakeholder_impact_reviewed",
    "human_agency_reviewed",
    "fairness_reviewed",
    "transparency_reviewed",
    "privacy_reviewed",
    "misuse_reviewed",
    "accountability_reviewed",
    "contestability_reviewed",
    "governance_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    """Authorize nonbinding ethics recommendations only after complete review."""
    context = context or {}
    if action in BLOCKED_ACTIONS:
        return {"allowed": False, "reason": "binding or coercive action is outside reference-system authority"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required ethics review", "missing": missing}

    blockers = []
    if context.get("material_harm_unresolved"):
        blockers.append("material stakeholder harm unresolved")
    if context.get("human_override_removed"):
        blockers.append("meaningful human override is absent")
    if context.get("disparate_impact_unresolved"):
        blockers.append("fairness or disparate-impact concern unresolved")
    if context.get("material_risk_hidden"):
        blockers.append("material risk is not transparently disclosed")
    if context.get("privacy_intrusion"):
        blockers.append("privacy intrusion unresolved")
    if context.get("misuse_path_unmitigated"):
        blockers.append("foreseeable misuse path unmitigated")
    if context.get("accountability_gap"):
        blockers.append("accountability ownership is unclear")
    if context.get("no_appeal_or_redress"):
        blockers.append("contestability or redress mechanism missing")

    if blockers:
        return {"allowed": False, "reason": "ethics governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "nonbinding recommendation approved after qualified human ethics review"}
