from selenium import webdriver

from virtual_greenhouse.api import GreenhouseApiClient
from virtual_greenhouse.device import Device, DeviceType

def before_all(context):
    context.api_client = GreenhouseApiClient(0, fatal=False)

    context.valid_sensor = Device("valid_sensor", DeviceType.SENSOR, None)
    context.valid_actuator = Device("valid_actuator", DeviceType.ACTUATOR, None)

    context.api_client.create_device(context.valid_sensor)
    context.api_client.create_device(context.valid_actuator)

def before_tag(context, tag):
    if tag == "frontend":
        context.driver = webdriver.Firefox()

        context.frontend_url = "https://se-frontend.fly.dev"

def after_tag(context, tag):
    if tag == "frontend":
        context.driver.quit()
