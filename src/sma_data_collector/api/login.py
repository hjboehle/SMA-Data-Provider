"""api.login"""

import logging
import os
import json
from api.send_request import send_request
from logger.config_logger import configure_logger


logger = logging.getLogger(__name__)


def get_session_id(ip_address: str) -> str:
    """
    Sends a POST request to obtain a session ID from a SMA device.

    Args:
        ip_address (str): The IP address of the SMA device.

    Returns:
        str: The session ID obtained from the SMA device, or an empty string if unsuccessful.
    """
    session_id = ""
    url = f"https://{ip_address}/dyn/login.json"
    request_attributes = {
        "headers": None,
        "data": None,
        "params": None,
        "json": {
            "right": os.environ["SMA_DEVICE_RIGHT"],
            "pass": os.environ["SMA_DEVICE_PASSWORD"]
        },
        "cert": None,
        "verify": False
    }
    response = send_request(ip_address, "POST", url, request_attributes)
    if response.status_code == 200:
        try:
            session_id = json.loads(response.text)["result"]["sid"]
            if session_id:
                logger.info("success: A valid session id was received")
            else:
                logger.error("failed: An invalid session id was received")
                session_id = ""
        except TypeError as err:
            logger.error(
                "failed: The session id could not be extracted from the response: %s",
                err
            )
        except KeyError as err:
            logger.error(
                "failed: The session id could not be extracted from the response: %s",
                err
            )
    else:
        logger.error(
            "failed: The session id could not be received due to an unsuccessful request"
        )
    return session_id


if __name__ == "__main__":
    configure_logger(log_level="INFO")
    logger.info("note: this file '%s' can not run directly", __file__)
