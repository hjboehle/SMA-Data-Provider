"""module arguments.test_arguments"""

import sys
import os
import pytest

sys.path.append(f"{os.getcwd()}/src/sma_data_provider")
from arguments.arguments import parse_arguments


def test_parse_arguments_with_valid_arguments():
    """
    test of the function parse_arguments with valid arguments
    """
    args = parse_arguments(["--ip_address", "192.168.1.1", "--tcp_port", "502"])
    assert args.ip_address == "192.168.1.1"
    assert args.tcp_port == 502


def test_parse_arguments_with_required_valid_arguments():
    """
    test of the function parse_arguments with required valid arguments
    """
    args = parse_arguments(["--ip_address", "192.168.1.1"])
    assert args.ip_address == "192.168.1.1"


def test_parse_arguments_without_required_arguments():
    """
    test of the function parse_arguments without required arguments
    """
    try:
        parse_arguments(["--tcp_port", "502"])
    except SystemExit:
        pass
    else:
        assert False, "Expected SystemExit, but no exception was raised"


def test_parse_arguments_without_any_argument():
    """
    test of the function parse_arguments with any arguments
    """
    try:
        parse_arguments([])
    except SystemExit:
        pass
    else:
        assert False, "Expected SystemExit, but no exception was raised"


def test_parse_arguments_with_an_invalid_argument():
    """
    test of the function parse_arguments with an invalid argument
    """
    try:
        parse_arguments(["--fake_argument", "xyz"])
    except SystemExit:
        pass
    else:
        assert False, "Expected SystemExit, but no exception was raised"


def test_parse_arguments_with_a_wrong_value_type():
    """
    test of the function parse_arguments with a wrong value type
    """
    try:
        parse_arguments(["--tcp_port", "fivehundredandtwo"])
    except SystemExit:
        pass
    else:
        assert False, "Expected SystemExit, but no exception was raised"


def test_parse_arguments_help_text(capfd):
    """
    test of the function parse_arguments helptext
    """
    with pytest.raises(SystemExit) as err:
        parse_arguments(["--help"])
    out, _ = capfd.readouterr()
    assert "The IP address of the MODBUS server" in out
    assert "The TCP port of the MODBUS server" in out
    assert err.type == SystemExit
    assert err.value.code == 0
