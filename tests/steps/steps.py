from behave import given, when, then

@then("the API should emit a {response_type} response with HTTP code {code}")
def api_response(context, response_type: str, code: int):
    print(f"Expected: {code}, actual: {context.api_client.response.status_code}")

    assert context.api_client.response.status_code == int(code)