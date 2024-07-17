Feature: Handling devices
    Scenario: Creating a device with a name that already exists
        Given a device with name valid_sensor exists
        When I try to create that device
        Then the API should emit a negative response with HTTP code 409

    Scenario: Trying to find a non-existing device by name
        Given a device with name non_existing_device does not exist
        When I try to find that device
        Then the API should emit a negative response with HTTP code 404

#    Scenario: Creating a device with a name that does not yet exist
#        Given a device with name non_existing_device does not exist
#        When I try to create a that device
#        Then the API should emit a positive response with HTTP code 201

    Scenario: Finding an existing device by name
        Given a device with name valid_sensor exists
        When I try to find that device
        Then the API should emit a positive response with HTTP code 200
