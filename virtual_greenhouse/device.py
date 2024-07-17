from enum import StrEnum

from .smart_device import SmartDevice
from .actuator import Actuator
from .sensor import Sensor

class DeviceType(StrEnum):
    SENSOR = "SENSOR"
    ACTUATOR = "ACTUATOR"
    SMART = "SMART"

class Device:
    def __init__(self, name: str, device_type: str, device: SmartDevice | Actuator | Sensor):
        self.name = name
        self.type = device_type
        self.device = device

    @staticmethod
    def from_device_type(name: str, device: SmartDevice | Actuator | Sensor):
        if isinstance(device, SmartDevice):
            return Device(name, DeviceType.SMART, device)
        elif isinstance(device, Actuator):
            return Device(name, DeviceType.ACTUATOR, device)
        elif isinstance(device, Sensor):
            return Device(name, DeviceType.SENSOR, device)

    @staticmethod
    def from_json(device: dict):
        device_name = device["name"]
        device_type = list(device["type"].keys())[0]

        if device_type == "SENSOR":
            return Device(device_name, DeviceType.SENSOR, Sensor())
        elif device_type == "ACTUATOR":
            return Device(device_name, DeviceType.ACTUATOR, Actuator())
        elif device_type == "SMART":
            return Device(device_name, DeviceType.SMART, SmartDevice())

    def to_json(self):
        return {
            "name": self.name,
            "type": {
                str(self.type): {}
            }
        }
