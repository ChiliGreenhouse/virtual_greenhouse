import arrow
from behave import given, when, then

from virtual_greenhouse.models.target_value import NewTargetValue, TargetValueType

@when("I try to set a new target value {value}")
def try_set_new_target_value(context, value: float):
    new_target = NewTargetValue(float(value), TargetValueType.CONSTANT)

    context.api_client.set_target(context.device, new_target)

@then("the value should be the current target value")
def should_be_new_target_value(context):
    created_timestamp = context.api_client.response.json()["data"]["timestamp"]

    targets = list(context.api_client.get_targets_of(context.device))

    assert arrow.get(created_timestamp) == targets[-1].timestamp