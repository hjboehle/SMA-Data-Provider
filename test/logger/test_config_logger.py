"""module test_config_logger"""

import logging
import sys
import os
from datetime import datetime

sys.path.append(f"{os.getcwd()}/src/sma_data_provider")
from logger.config_logger import configure_logger


def test_configure_logger(caplog):
    """
    Test the configure_logger function.

    This test function configures the logger using the configure_logger function with a log 
    level of DEBUG. It checks whether the logger has been configured correctly, if the log 
    outputs are working correctly and if the date format in the log outputs is correct.

    Args:
        caplog: Pytest fixture for capturing log outputs.

    Raises:
        AssertionError: If any of the test conditions fail.

    """
    configure_logger(log_level=logging.DEBUG)

    # Check whether the logger has been configured correctly
    logger = logging.getLogger()
    assert logger.level == logging.DEBUG

    # Check whether the log outputs are working correctly
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")

    # Check whether the date format in the log outputs is correct
    current_year = datetime.now().year
    for record in caplog.records:
        assert record.levelname in caplog.text
        assert record.message in caplog.text
        assert f"{current_year}-" in record.asctime
