from AGENTS.stakeholder_impact_agent import StakeholderImpactAgent
from AGENTS.human_agency_agent import HumanAgencyAgent
from AGENTS.fairness_review_agent import FairnessReviewAgent
from AGENTS.transparency_agent import TransparencyAgent
from AGENTS.governance_agent import GovernanceAgent
from AGENTS.accountability_agent import AccountabilityAgent
A=[StakeholderImpactAgent(),HumanAgencyAgent(),FairnessReviewAgent(),TransparencyAgent(),GovernanceAgent(),AccountabilityAgent()]
def run(c): return {"system":"F80","results":[a.run(c) for a in A],"binding_decision":False,"robot_control":False}
