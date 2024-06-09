from .sensor import Sensor
from .actuator import Actuator
from .environment_value import EnvironmentValue

import math
from datetime import timedelta

class SmartDevice:
    def __init__(self, value: EnvironmentValue=None, steering_rate=None):
        self.value = value or EnvironmentValue()
        self.sensor = Sensor(self.value)
        self.actuator = Actuator(self.value) 
        self.target_value = None
        self.steering_rate = steering_rate or 0.1

    def set_target_value(self, value: float):
        self.target_value = value

    def update(self, delta_time: timedelta):
        current_value = self.sensor.get_measurement()
        diff = target_value - current_value
        elapsed_seconds = delta_time.total_seconds()
        direction = math.copysign(diff)

        new_value = current_value + (direction * steering_rate * elapsed_seconds)

        self.actuator.set_value(new_value)
             
