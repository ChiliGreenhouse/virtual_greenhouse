from behave import given, when, then

from virtual_greenhouse.models.datapoint import NewDatapoint
from virtual_greenhouse.device import Device

def device_exists(context, name, should_exist):
    devices = context.api_client.get_devices()

    device_exists = False
    for device in devices:
        if device.name == name:
            context.device = device
            device_exists = True

    if not device_exists:
        context.device = Device(name, "SENSOR", None)

    assert device_exists == should_exist 

@given("a device with name {name} exists")
def ensure_device_exists(context, name: str):
    device_exists(context, name, True)

@given("a device with name {name} does not exist")
def ensure_device_exists(context, name: str):
    device_exists(context, name, False)

@given("that device is of type {device_type}")
def ensure_device_type(context, device_type: str):
    assert context.device.type == device_type.upper()

@given("that device is not of type {device_type}")
def ensure_device_type(context, device_type: str):
    assert context.device.type != device_type.upper()

@when("I try to find that device")
def try_find_device(context):
    print(f"NAME IS {context.device.name}")

    context.api_client.get_device_by_name(context.device.name)

@when("I try to create that device")
def try_create_device(context):
    context.api_client.create_device(context.device)