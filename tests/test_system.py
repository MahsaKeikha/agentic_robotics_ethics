from orchestration.orchestrator import run
from safety.gate import authorize
def test_run():
    r=run({"objective":"x"}); assert r["binding_decision"] is False and r["robot_control"] is False
def test_gate(): assert authorize("remove_human_override")["allowed"] is False
