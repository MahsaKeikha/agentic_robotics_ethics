def authorize(action):
    blocked={"robot_command","binding_policy_decision","remove_human_override","hide_material_risk"}
    return {"allowed":action not in blocked,"reason":"outside responsible review scope" if action in blocked else "reviewable"}
