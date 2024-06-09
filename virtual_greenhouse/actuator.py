from .environment_value import EnvironmentValue

class Actuator:
    def __init__(self, value: EnvironmentValue=None):
        self.value = value or EnvironmentValue("", "", 0)

    def set_value(value: float):
        self.value.set_value(value) 
