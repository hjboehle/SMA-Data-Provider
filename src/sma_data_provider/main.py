"""module main"""

import argparse


def main():
    """
    The main function of the SMA data provider.
    
    This function is called when the program is started.
    
    Arguments:
        ip_address: The IP address of the MODBUS server.
        tcp_port: The TCP port of the MODBUS server.
    
    Returns:
        None.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ip_address",
        type=str,
        required=True,
        help="The IP address of the MODBUS server"
    )
    parser.add_argument(
        "--tcp_port",
        type=int,
        required=False,
        help="The TCP port of the MODBUS server"
    )
    args = parser.parse_args()
    ip_address = args.ip_address
    tcp_port = args.tcp_port
    print(f"Hello developer, the IP address is {ip_address} and the TCP port is {tcp_port}")


if __name__ == "__main__":
    main()
