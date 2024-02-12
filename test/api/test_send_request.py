"""module arguments.test_arguments"""

import sys
import os
import requests
import requests_mock

sys.path.append(f"{os.getcwd()}/src/sma_data_collector")
from api.send_request import send_request


def test_send_request_success():
    # Mocking the request method
    headers = {
                "User-Agent": "SMA device data collector",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/json;charset=utf-8",
                "Origin": "dummy_ip",
                "Connection": "keep-alive",
                "Referer": "dummy_ip/",
                "Cookie": "tmhDynamicLocale.locale=%22de%22",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            }
    with requests_mock.Mocker() as m:
        m.post(
            "https://dummy_ip/dyn/login.json",
            json={
                "result": {
                    "sid": "dummy_session_id"
                }
            },
            headers=headers,
            status_code=200
        )
        response = send_request(
            "dummy_ip",
            "POST",
            "https://dummy_ip/dyn/login.json",
            {
                "data": None,
                "headers": headers,
                "params": None,
                "json": None,
                "cert": None,
                "verify": False
            }
        )
    assert response.status_code == 200
    assert response.json()["result"]["sid"] == "dummy_session_id"


def test_send_request_failure():
    # Mocking the request method to raise a HTTPError
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
                "headers": None,
                "params": None,
                "json": None,
                "cert": None,
                "verify": False
            }
        )
    assert response.status_code == 500
