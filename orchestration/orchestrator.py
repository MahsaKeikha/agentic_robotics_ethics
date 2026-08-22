from AGENTS.accountability_agent import AccountabilityAgent
from AGENTS.fairness_review_agent import FairnessReviewAgent
from AGENTS.governance_agent import GovernanceAgent
from AGENTS.human_agency_agent import HumanAgencyAgent
from AGENTS.stakeholder_impact_agent import StakeholderImpactAgent
from AGENTS.transparency_agent import TransparencyAgent
from safety.gate import authorize

AGENTS = [
    StakeholderImpactAgent(),
    HumanAgencyAgent(),
    FairnessReviewAgent(),
    TransparencyAgent(),
    GovernanceAgent(),
    AccountabilityAgent(),
]


def run(context: dict) -> dict:
    """Run six ethics specialists and apply the fail-closed recommendation gate."""
    results = [agent.run(context) for agent in AGENTS]
    governance = authorize("recommendation_release", context)
    return {
        "system": "F80",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "binding_decision": False,
        "robot_control": False,
        "autonomous_enforcement": False,
    }
