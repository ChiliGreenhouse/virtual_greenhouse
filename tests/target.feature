Feature: Handling target values
    Scenario: Setting a new target value for an existing actuator device
        Given a device with name valid_actuator exists
        And that device is of type actuator
        When I try to set a new target value 123
        Then the API should emit a positive response with HTTP code 200
        And the value should be the current target value

    Scenario: Setting a new target value for an existing non-actuator device
        Given a device with name valid_sensor exists
        And that device is not of type actuator
        When I try to set a new target value 123
        Then the API should emit a negative response with HTTP code 422

    Scenario: Setting a new target value for a non-existing device
        Given a device with name invalid_device does not exist
        When I try to set a new target value 123
        Then the API should emit a negative response with HTTP code 404