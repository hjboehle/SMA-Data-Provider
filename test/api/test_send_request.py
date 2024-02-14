"""module api.test_send_request"""

import sys
import os
import requests
import requests_mock

sys.path.append(f"{os.getcwd()}/src/sma_data_collector")
from api.send_request import send_request


DUMMY_IP_ADDRESS = "dummy_ip"
HEADERS_REQUEST = {
    "User-Agent": "SMA device data collector",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": f"{DUMMY_IP_ADDRESS}",
    "Connection": "keep-alive",
    "Referer": f"{DUMMY_IP_ADDRESS}/",
    "Cookie": "tmhDynamicLocale.locale=%22de%22",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}


def test_send_request_success() -> None:
    """
    Tests successful login request with "send_request" function.
    
    This test mocks the "requests" library using "requests_mock" to simulate a successful POST
    request to the login endpoint. It then calls the "send_request" function with the expected
    parameters and asserts that the response status code and session ID are correct.
    
    Args:
        None
    
    Returns:
        None
    """
    with requests_mock.Mocker() as m:
        m.post(
            "https://dummy_ip/dyn/login.json",
            json={
                "result": {
                    "sid": "dummy_session_id"
                }
            },
            headers=HEADERS_REQUEST,
            status_code=200
        )
        response = send_request(
            "dummy_ip",
            "POST",
            "https://dummy_ip/dyn/login.json",
            {
                "data": None,
                "headers": HEADERS_REQUEST,
                "params": None,
                "json": {
                    "right": "usr",
                    "pass": "very_secret"
                },
                "cert": None,
                "verify": False
            }
        )
    assert response.status_code == 200
    assert response.json()["result"]["sid"] == "dummy_session_id"


def test_send_request_failure_http_error() -> None:
    """
    Tests failed login request with "send_request" function.
    This test mocks the "requests" library using "requests_mock" to simulate a failed POST
    request to the login endpoint by raising an "HTTPError". It then calls the "send_request"
    function with the expected parameters and asserts that the response status code is 500
    and the reason is "HTTP error".
    
    Args:
        None
    
    Returns:
        None
    """
    with requests_mock.Mocker() as m:
        m.post(
            "https://dummy_ip/dyn/login.json",
            exc=requests.exceptions.HTTPError
        )
        response = send_request(
            "dummy_ip",
            "POST",
            "https://dummy_ip/dyn/login.json",
            {
                "data": None,
                "headers": HEADERS_REQUEST,
                "params": None,
                "json": {
                    "right": "usr",
                    "pass": "very_secret"
                },
                "cert": None,
                "verify": False
            }
        )
    assert response.status_code == 500
    assert response.reason == "HTTP error"


def test_send_request_failure_connection_error() -> None:
    """
    Tests failed login request with "send_request" function.
    This test mocks the "requests" library using "requests_mock" to simulate a failed POST
    request to the login endpoint by raising an "ConnectionError". It then calls the "send_request"
    function with the expected parameters and asserts that the response status code is 500
    and the reason is "connection error".
    
    Args:
        None
    
    Returns:
        None
    """
    with requests_mock.Mocker() as m:
        m.post(
            "https://dummy_ip/dyn/login.json",
            exc=requests.exceptions.ConnectionError
        )
        response = send_request(
            "dummy_ip",
            "POST",
            "https://dummy_ip/dyn/login.json",
            {
                "data": None,
                "headers": HEADERS_REQUEST,
                "params": None,
                "json": {
                    "right": "usr",
                    "pass": "very_secret"
                },
                "cert": None,
                "verify": False
            }
        )
    assert response.status_code == 500
    assert response.reason == "connection error"


def test_send_request_failure_timeout_error() -> None:
    """
    Tests failed login request with "send_request" function.
    This test mocks the "requests" library using "requests_mock" to simulate a failed POST
    request to the login endpoint by raising an "Timeout". It then calls the "send_request"
    function with the expected parameters and asserts that the response status code is 500
    and the reason is "timeout error".
    
    Args:
        None
    
    Returns:
        None
    """
    with requests_mock.Mocker() as m:
        m.post(
            "https://dummy_ip/dyn/login.json",
            exc=requests.exceptions.Timeout
        )
        response = send_request(
            "dummy_ip",
            "POST",
            "https://dummy_ip/dyn/login.json",
            {
                "data": None,
                "headers": HEADERS_REQUEST,
                "params": None,
                "json": {
                    "right": "usr",
                    "pass": "very_secret"
                },
                "cert": None,
                "verify": False
            }
        )
    assert response.status_code == 500
    assert response.reason == "timeout error"


def test_send_request_failure_too_many_redirections() -> None:
    """
    Tests failed login request with "send_request" function.
    This test mocks the "requests" library using "requests_mock" to simulate a failed POST
    request to the login endpoint by raising an "TooManyRedirects". It then calls the
    "send_request" function with the expected parameters and asserts that the response status
    code is 500 and the reason is "to many redirections".
    
    Args:
        None
    
    Returns:
        None
    """
    with requests_mock.Mocker() as m:
        m.post(
            "https://dummy_ip/dyn/login.json",
            exc=requests.exceptions.TooManyRedirects
        )
        response = send_request(
            "dummy_ip",
            "POST",
            "https://dummy_ip/dyn/login.json",
            {
                "data": None,
                "headers": HEADERS_REQUEST,
                "params": None,
                "json": {
                    "right": "usr",
                    "pass": "very_secret"
                },
                "cert": None,
                "verify": False
            }
        )
    assert response.status_code == 500
    assert response.reason == "to many redirections"


def test_send_request_failure_request_exception() -> None:
    """
    Tests failed login request with "send_request" function.
    This test mocks the "requests" library using "requests_mock" to simulate a failed POST
    request to the login endpoint by raising an "RequestException". It then calls the
    "send_request" function with the expected parameters and asserts that the response status
    code is 500 and the reason is "request exception".
    
    Args:
        None
    
    Returns:
        None
    """
    with requests_mock.Mocker() as m:
        m.post(
            "https://dummy_ip/dyn/login.json",
            exc=requests.exceptions.RequestException
        )
        response = send_request(
            "dummy_ip",
            "POST",
            "https://dummy_ip/dyn/login.json",
            {
                "data": None,
                "headers": HEADERS_REQUEST,
                "params": None,
                "json": {
                    "right": "usr",
                    "pass": "very_secret"
                },
                "cert": None,
                "verify": False
            }
        )
    assert response.status_code == 500
    assert response.reason == "request exception"
