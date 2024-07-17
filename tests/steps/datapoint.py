import arrow
from behave import when, then, given

from virtual_greenhouse.models.datapoint import NewDatapoint

@when("I record a datapoint with value {datapoint}")
def record_datapoint(context, datapoint: float):
    new_datapoint = NewDatapoint(float(datapoint))
    context.api_client.create_datapoint(context.device, new_datapoint)

@then("that datapoint should be recorded")
def datapoint_should_be_there(context):
    created_timestamp = context.api_client.response.json()["data"]["timestamp"]

    datapoints = list(context.api_client.get_datapoints_of(context.device))

    assert arrow.get(created_timestamp).datetime == datapoints[-1].timestamp