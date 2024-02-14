"""module api.test_login"""

# pylint: disable=unused-argument

import sys
import os
import pytest

sys.path.append(f"{os.getcwd()}/src/sma_data_collector")
from api.login import get_session_id


@pytest.fixture(name="valid_session_id")
def mock_send_request_success_valid_session_id(requests_mock) -> None:
    """
    Fixture to mock a successful request with a valid session ID.

    Args:
        requests_mock: The fixture provided by the requests-mock library to mock HTTP requests.

    Returns:
        None
    """
    response_data = {"result": {"sid": "valid_session_id"}}
    requests_mock.post('https://dummy_ip/dyn/login.json', json=response_data)


@pytest.fixture(name="invalid_session_id")
def mock_send_request_success_invalid_session_id(requests_mock) -> None:
    """
    Fixture to mock a successful request with an invalid session ID.

    Args:
        requests_mock: The fixture provided by the requests-mock library to mock HTTP requests.

    Returns:
        None
    """
    response_data = {"result": {"sid": None}}
    requests_mock.post('https://dummy_ip/dyn/login.json', json=response_data)


@pytest.fixture(name="type_error")
def mock_send_request_success_type_error(requests_mock) -> None:
    """
    Fixture to mock a successful request with a TypeError exception.

    Args:
        requests_mock: The fixture provided by the requests-mock library to mock HTTP requests.

    Returns:
        None
    """
    response_data = {"fake": None}
    requests_mock.post('https://dummy_ip/dyn/login.json', json=response_data)


@pytest.fixture(name="key_error")
def mock_send_request_success_key_error(requests_mock) -> None:
    """
    Fixture to mock a successful request with a KeyError exception.

    Args:
        requests_mock: The fixture provided by the requests-mock library to mock HTTP requests.

    Returns:
        None
    """
    response_data = "<html><body>no json response</body></html>"
    requests_mock.post('https://dummy_ip/dyn/login.json', json=response_data)


@pytest.fixture(name="failed_request")
def mock_send_request_failure(requests_mock) -> None:
    """
    Fixture to mock a failure request.

    Args:
        requests_mock: The fixture provided by the requests-mock library to mock HTTP requests.

    Returns:
        None
    """
    requests_mock.post('https://dummy_ip/dyn/login.json', status_code=500)


def test_get_session_id_success_valid_session_id(valid_session_id) -> None:
    """
    Test the get_session_id function with a successful request and valid session ID.

    Args:
        mock_send_request_success_valid_session_id: Fixture to mock a successful request with a
        valid session ID.

    Returns:
        None
    """
    ip_address = 'dummy_ip'
    session_id = get_session_id(ip_address)
    assert session_id == "valid_session_id"


def test_get_session_id_success_invalid_session_id(invalid_session_id) -> None:
    """
    Test the get_session_id function with a successful request and invalid session ID.

    Args:
        mock_send_request_success_valid_session_id: Fixture to mock a successful request with a
        invalid session ID.

    Returns:
        None
    """
    ip_address = 'dummy_ip'
    session_id = get_session_id(ip_address)
    assert session_id == ""


def test_get_session_id_success_type_error(type_error) -> None:
    """
    Test the get_session_id function with a successful request and TypeError exception.

    Args:
        mock_send_request_success_valid_session_id: Fixture to mock a successful request with a
        TypeError.

    Returns:
        None
    """
    ip_address = 'dummy_ip'
    session_id = get_session_id(ip_address)
    assert session_id == ""


def test_get_session_id_success_key_error(key_error) -> None:
    """
    Test the get_session_id function with a successful request and KeyError exception.

    Args:
        mock_send_request_success_valid_session_id: Fixture to mock a successful request with a
        KeyError.

    Returns:
        None
    """
    ip_address = 'dummy_ip'
    session_id = get_session_id(ip_address)
    assert session_id == ""


def test_get_session_id_failure(failed_request) -> None:
    """
    Test the get_session_id function with a failure request.

    Args:
        mock_send_request_success_valid_session_id: Fixture to mock a failure request.

    Returns:
        None
    """
    ip_address = 'dummy_ip'
    session_id = get_session_id(ip_address)
    assert session_id == ""
