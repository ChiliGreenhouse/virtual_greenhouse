from datetime import datetime
from typing import NewType

import arrow

class NewDatapoint:
    def __init__(self, value: float):
        self.value = value

    def to_json(self):
        return {
            "value": self.value
        }

class Datapoint:
    def __init__(self, timestamp: datetime, value: float):
        self.timestamp = timestamp
        self.value = value

    @staticmethod
    def from_json(json_dict: dict) -> "Datapoint":
        return Datapoint(
            arrow.get(json_dict["timestamp"]).datetime,
            json_dict["value"]
        ) 

    def __repr__(self):
        return f"Datapoint({self.timestamp}, {self.value})"
