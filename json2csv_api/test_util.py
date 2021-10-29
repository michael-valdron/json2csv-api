

from json2csv_api.util import error_response


def test_error_response() -> None:
    message = "Something went wrong!"
    expected_one = "{\"error\": {\"message\": \"%s\"}}" % message
    expected_two = "{\"error\": {\"message\": \"%s\", \"code\": 500}}" % message
    assert expected_one == error_response(message)
    assert expected_two == error_response(message, code=500)
