"""module main"""

import logging
from arguments.arguments import parse_arguments
from logger.config_logger import configure_logger

def main() -> None:
    """
    The main function of the SMA data provider.
    
    This function is called when the program is started.
    
    Args:
        args: The parsed command-line arguments.
    
    Returns:
        Nothing.
    """
    configure_logger()
    logger = logging.getLogger(__name__)
    logger.info("success: script hast startet")
    args = parse_arguments()
    if args.log_level:
        configure_logger(log_level=args.log_level)
    ip_address = args.ip_address
    tcp_port = args.tcp_port
    print(f"Hello developer, the IP address is {ip_address} and the TCP port is {tcp_port}")


if __name__ == "__main__":
    main()
