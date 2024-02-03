"""logger.config_logger"""

import logging
from logging.handlers import RotatingFileHandler


def configure_logger(log_file_path="app.log", log_level=logging.INFO):
    """
    Configures the logger with a flexible configuration.

    Args:
        log_file_path (str): The path to the log file. Defaults to 'app.log'.
        log_level (int): The logging level. Defaults to logging.INFO.

    Returns:
        logging.Logger: The configured logger instance.
    """
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level))

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    # Create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Create file handler and set level (optional)
    file_handler = RotatingFileHandler(log_file_path, maxBytes=10*1024*1024, backupCount=5)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    configured_logger = configure_logger(log_level="INFO")
    configured_logger.info("note: this file '%s' can not run directly", __file__)
