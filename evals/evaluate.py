def evaluate(r): return {"passed":r.get("binding_decision") is False and r.get("robot_control") is False and len(r.get("results",[]))==6}
