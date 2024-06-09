from .sensor import Sensor
from .smart_device import SmartDevice
from .actuator import Actuator
from .device import DeviceType, Device
from .environment_value import EnvironmentValue
from . import api

from datetime import datetime, timedelta

class Greenhouse:
    def __init__(self, greenhouse_id: int, tick_rate: timedelta=None, api_client=None):
        self.api_client = api_client or api.GreenhouseApiClient(greenhouse_id)
        self.devices = []
        self.current_timestamp = datetime.now()
        self.tick_rate = tick_rate or timedelta(seconds=1)

    def add_device(self, name: str, device: SmartDevice | Actuator | Sensor):
        self.devices.append(Device.from_device_type(name, device))

    def fetch_target_values(self):
        for device in self.devices:
            if device.type != DeviceType.SENSOR:
                target_value = self.api_client.get_current_target_of(device)
                if target_value is not None:
                    device.target_value = target_value.value
                yield self.api_client.get_targets_of(device)


    def send_sensor_values(self):
        for device in self.devices:
            if device.type == DeviceType.SENSOR:
                new_datapoint = NewDatapoint(device.get_measurement())
            elif device.type == DeviceType.SMART:
                new_datapoint = NewDatapoint(device.sensor.get_measurement())

            self.api_client.create_datapoint(device, new_datapoint)

    def tick(self):
        self.current_timestamp += self.tick_rate

        for device in devices:
            if device.type == DeviceType.SMART:
                device.update(self.tick_rate)
        
