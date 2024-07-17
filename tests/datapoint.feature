Feature: Handling datapoints
    Scenario: Creating a valid datapoint for an existing sensor device
        Given a device with name valid_sensor exists
        And that device is of type sensor 
        When I record a datapoint with value 420
        Then the API should emit a positive response with HTTP code 200 
        And that datapoint should be recorded

    Scenario: Creating a valid datapoint for an existing non-sensor device
        Given a device with name valid_actuator exists
        And that device is not of type sensor
        When I record a datapoint with value 420
        Then the API should emit a negative response with HTTP code 422

    Scenario: Creating a valid datapoint for a non-existing device
        Given a device with name non_existing_device does not exist
        When I record a datapoint with value 420
        Then the API should emit a negative response with HTTP code 404