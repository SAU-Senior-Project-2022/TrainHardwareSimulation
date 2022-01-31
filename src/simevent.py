from enum import Enum

class SimEventType(str, Enum):
    Train = "train",
    Comm_Failure = "comm_failure",
    Hard_Failure = "hard_failure"

class SimEvent():
    def __init__(self, obj: dict) -> None:
        self.type: SimEventType = SimEventType(obj.get("type"))
        match self.type:
            case SimEventType.Train | SimEventType.Comm_Failure:
                self.description = obj.get("description")
                self.start_time = obj.get("start_time")
                self.duration = None if not obj.get("duration") else float(obj.get("duration"))
                self.end_time = obj.get("end_time")
            case SimEventType.Hard_Failure:
                self.description = obj.get("description")
                self.start_time = obj.get("start_time")
                self.duration = None if not obj.get("duration") else float(obj.get("duration"))
                self.end_time = obj.get("end_time")
            case _:
                raise TypeError("Invalid SimEventType")