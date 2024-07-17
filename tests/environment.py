from virtual_greenhouse.api import GreenhouseApiClient
from virtual_greenhouse.device import Device, DeviceType

def before_all(context):
    context.api_client = GreenhouseApiClient(0, fatal=False)

    context.valid_sensor = Device("valid_sensor", DeviceType.SENSOR, None)
    context.valid_actuator = Device("valid_actuator", DeviceType.ACTUATOR, None)

    context.api_client.create_device(context.valid_sensor)
    context.api_client.create_device(context.valid_actuator)

    if hasattr(context, "tags") and "frontend" in context.tags:
        ... # Init selenium