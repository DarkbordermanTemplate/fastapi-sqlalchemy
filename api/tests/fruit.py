import pytest
from models import init_db
from tests import AssertRequest, AssertResponse, assert_request, clean_db

ROUTE = "/fruit"

HEADERS = {"Content-Type": "Application/json"}

GET_INPUT = {
    "success": AssertRequest(None, {"name": "apple"}),
    "fail_notexist": AssertRequest(None, {"name": "banana"}),
}

GET_OUTPUT = {
    "success": AssertResponse({"name": "apple", "count": 1}, 200),
    "fail_notexist": AssertResponse("Bad Request", 400),
}


@pytest.mark.parametrize("test_type", GET_INPUT.keys())
def test_get(test_type):
    clean_db()
    init_db()
    assert_request("GET", ROUTE, GET_INPUT[test_type], GET_OUTPUT[test_type])


POST_INPUT = {
    "success": AssertRequest(HEADERS, {"name": "banana"}),
    "fail_already_exist": AssertRequest(HEADERS, {"name": "apple"}),
}

POST_OUTPUT = {
    "success": AssertResponse("OK", 200),
    "fail_already_exist": AssertResponse("Bad Request", 400),
}


@pytest.mark.parametrize("test_type", POST_INPUT.keys())
def test_post(test_type):
    clean_db()
    init_db()
    assert_request("POST", ROUTE, POST_INPUT[test_type], POST_OUTPUT[test_type])


DELETE_INPUT = {
    "success": AssertRequest(HEADERS, {"name": "apple"}),
    "fail_notexist": AssertRequest(HEADERS, {"name": "banana"}),
}

DELETE_OUTPUT = {
    "success": AssertResponse("OK", 200),
    "fail_notexist": AssertResponse("Bad Request", 400),
}


@pytest.mark.parametrize("test_type", DELETE_OUTPUT.keys())
def test_delete(test_type):
    clean_db()
    init_db()
    assert_request("DELETE", ROUTE, DELETE_INPUT[test_type], DELETE_OUTPUT[test_type])


PUT_INPUT = {
    "success": AssertRequest(HEADERS, {"name": "apple", "count": 2}),
    "fail_notexist": AssertRequest(HEADERS, {"name": "banana", "count": 2}),
}

PUT_OUTPUT = {
    "success": AssertResponse("OK", 200),
    "fail_notexist": AssertResponse("Bad Request", 400),
}


@pytest.mark.parametrize("test_type", PUT_OUTPUT.keys())
def test_put(test_type):
    clean_db()
    init_db()
    assert_request("PUT", ROUTE, PUT_INPUT[test_type], PUT_OUTPUT[test_type])
