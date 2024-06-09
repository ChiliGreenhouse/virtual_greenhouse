from datetime import datetime
from enum import StrEnum

import arrow

class TargetValueType(StrEnum):
    CONSTANT = "CONSTANT"

class TargetValue:
    def __init__(self, timestamp: datetime, value_type: TargetValueType, value):
        self.timestamp = timestamp
        self.value_type = value_type
        self.value = value


    @staticmethod
    def from_json(json: dict):
        value = json["value"]
        value_type = list(value.keys())[0]

        return TargetValue(
            arrow.get(json["timestamp"]).datetime,
            value_type,
            value[value_type]
        )

    def __repr__(self):
        return f"TargetValue({self.timestamp}, {self.value_type}, {self.value})"
