from orchestration.orchestrator import run
from safety.gate import authorize


def valid_context():
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


def test_reference_system_never_controls_or_enforces():
    result = run(valid_context())
    assert result["binding_decision"] is False
    assert result["robot_control"] is False
    assert result["autonomous_enforcement"] is False


def test_complete_review_can_release_nonbinding_recommendation():
    assert run(valid_context())["release_allowed"] is True


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_binding_policy_decision_is_never_authorized():
    assert authorize("binding_policy_decision", valid_context())["allowed"] is False


def test_material_harm_blocks_release():
    context = valid_context()
    context["material_harm_unresolved"] = True
    assert run(context)["release_allowed"] is False


def test_disparate_impact_blocks_release():
    context = valid_context()
    context["disparate_impact_unresolved"] = True
    assert run(context)["release_allowed"] is False


def test_hidden_material_risk_blocks_release():
    context = valid_context()
    context["material_risk_hidden"] = True
    assert run(context)["release_allowed"] is False


def test_missing_redress_blocks_release():
    context = valid_context()
    context["no_appeal_or_redress"] = True
    assert run(context)["release_allowed"] is False
