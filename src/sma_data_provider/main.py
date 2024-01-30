"""module main"""

from arguments.arguments import parse_arguments


def main() -> None:
    """
    The main function of the SMA data provider.
    
    This function is called when the program is started.
    
    Args:
        args: The parsed command-line arguments.
    
    Returns:
        Nothing.
    """
    args = parse_arguments()
    ip_address = args.ip_address
    tcp_port = args.tcp_port
    print(f"Hello developer, the IP address is {ip_address} and the TCP port is {tcp_port}")


if __name__ == "__main__":
    main()
