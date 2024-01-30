"""module arguments.arguments"""

import argparse


def parse_arguments(args=None) -> argparse.Namespace:
    """
    Parses command-line arguments for the Modbus TCP client.
    
    This function parses the command-line arguments and returns a dictionary containing the 
    parsed arguments.
    
    Returns:
        A dictionary containing the parsed arguments.
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
    return parser.parse_args(args)
