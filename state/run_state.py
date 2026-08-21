from dataclasses import dataclass
@dataclass
class RunState: status:str="planned"; human_decision_owner:bool=True
