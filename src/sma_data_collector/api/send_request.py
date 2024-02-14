"""api.sendrequest"""

import logging
import requests
from logger.config_logger import configure_logger


logger = logging.getLogger(__name__)


def _get_error_response(status_code: int, reason: str) -> requests.Response:
    """
    Creates a custom error response object with the specified status code, reason, and content.

    Args:
        status_code (int): The HTTP status code of the response.
        reason (str): The reason phrase associated with the status code.
        content (str): The content or error message associated with the response.

    Returns:
        requests.Response: A custom response object representing the error response.
    """
    error_response = requests.Response()
    error_response.status_code = status_code
    error_response.reason = reason
    return error_response


def send_request(
        ip_address: str,
        method: str, url: str,
        request_attributes: dict = None
    ) -> requests.Response:
    """
    Send a HTTP request using the requests library.
    
    Args:
        method (str): The HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE').
        url (str): The URL of the request.
        request_attributes (dict): Attributes (headers, data, params, ...) for the the request.

    Returns:
        requests.Response: The response object.
    """
    if not request_attributes["data"]:
        request_attributes["data"] = None
    request_attributes["default_headers"] = {
        "User-Agent": "SMA device data collector",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json;charset=utf-8",
        "Origin": f"{ip_address}",
        "Connection": "keep-alive",
        "Referer": f"{ip_address}/",
        "Cookie": "tmhDynamicLocale.locale=%22de%22",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    if request_attributes["headers"]:
        request_attributes["headers"].update(request_attributes["default_headers"])
    request_method = getattr(requests, method.lower())
    try:
        response = request_method(
            url,
            headers=request_attributes["headers"],
            data=request_attributes["data"],
            params=request_attributes["params"],
            json=request_attributes["json"],
            cert=request_attributes["cert"],
            verify=request_attributes["verify"],
            timeout = 30
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logger.error("failed: The request failed with the following HTTP error: %s", err)
        return _get_error_response(500, "HTTP error")
    except requests.exceptions.ConnectionError as err:
        logger.error("failed: The request failed with the following connection error: %s", err)
        return _get_error_response(500, "connection error")
    except requests.exceptions.Timeout as err:
        logger.error("failed: The request failed with the following timeout error: %s", err)
        return _get_error_response(500, "timeout error")
    except requests.exceptions.TooManyRedirects as err:
        logger.error("failed: The request failed with the to many redirections: %s", err)
        return _get_error_response(500, "to many redirections")
    except requests.exceptions.RequestException as err:
        logger.error("failed: The request failed with the following error: %s", err)
        return _get_error_response(500, "request exception")
    logger.info("success: Response received")
    return response


if __name__ == "__main__":
    configure_logger(log_level="INFO")
    logger.info("note: this file '%s' can not run directly", __file__)
