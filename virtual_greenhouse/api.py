import requests

from typing import Iterable

from . import greenhouse 
from .sensor import Sensor
from .smart_device import SmartDevice
from .actuator import Actuator
from .models.datapoint import Datapoint, NewDatapoint
from .models.target_value import TargetValue
from .device import Device

class GreenhouseApiClient:
    def __init__(self, greenhouse_id: int, backend_url: str="https://se-backend.fly.dev"):
        self.url = backend_url.rstrip("/")
        self.url += f"/api/v0/gh/{greenhouse_id}"

        self.session = requests.Session()

    def call_api(self, method: str, path: str, **kwargs):
        path = path.lstrip("/")

        response = self.session.request(method, f"{self.url}/{path}")

        if not response.ok:
            raise Exception(f"Api call to {path} failed with code {response.status_code}")

        return response.json()

    def get_devices(self) -> Iterable[Device]:
        devices = self.call_api("get", "devices")

        for device in devices["data"]:
            yield Device.from_json(device)

    def create_device(self, device: Device) -> None:
        self.call_api("post", "devices", data=device.to_json()) 

    def get_device_by_name(self, name: str) -> Device:
        device = self.call_api("get", f"devices/{device.name}")

        return Device.from_json(device)
        
    def get_datapoints_of(self, device: Device) -> Iterable[Datapoint]:
        devices = self.call_api("get", f"devices/{device.name}/datapoints")

        for device in devices["data"]:
            yield Datapoint.from_json(device)

    def create_datapoint(self, device: Device, datapoint: NewDatapoint) -> None:
        self.call_api("post", f"devices/{device.name}/datapoints", data=datapoint.to_json())

    def get_current_target_of(self, device: Device):
        targets = self.call_api("get", f"devices/{device.name}/targets/current")

    def get_targets_of(self, device: Device) -> Iterable[Datapoint]:
        targets = self.call_api("get", f"devices/{device.name}/targets")["data"]

        for target in targets:
            yield TargetValue.from_json(target)
        
    def get_greenhouse() -> greenhouse.Greenhouse:
        gh = greenhouse.Greenhouse()

        gh.devices = self.get_devices()

        return gh
