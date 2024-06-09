from enum import Enum

class EnvironmentValue:
    def __init__(self, name: str, unit: str, value: float=None):
        self.name = name
        self.unit = unit
        self.value = value

    def get_value(self):
        return self.value
