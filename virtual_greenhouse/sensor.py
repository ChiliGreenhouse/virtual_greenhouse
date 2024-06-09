import random
from enum import Enum
from datetime import timedelta

from .environment_value import EnvironmentValue

class Sensor:
    def __init__(self, value: EnvironmentValue=None):
        self.value = value or EnvironmentValue("", "", 0)

    def get_measurement(self):
        return self.value.get_value()

