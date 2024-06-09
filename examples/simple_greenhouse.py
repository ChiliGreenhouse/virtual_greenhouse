from virtual_greenhouse import *

if __name__ == "__main__":
    greenhouse = Greenhouse(0)

    soil_moisture = EnvironmentValue("soil_moisture", "", 0)
    brightness = EnvironmentValue("brightness", "%", 100)

    #soil_moisture_device = SmartDevice(soil_moisture)
    light = Actuator(brightness)

    #greenhouse.add_device("soil_moisture", soil_moisture_device)
    greenhouse.add_device("light", light)

    devices = greenhouse.api_client.get_devices()

    for device in devices:
        print(device.name)

    for target_values in greenhouse.fetch_target_values():
        print(list(target_values))
