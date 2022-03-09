import os

import py
import pytest
from conftest import db_conn
from conftest import mock_env_missing
from conftest import mock_env_user


def test_addition():
    """_summary_"""
    assert (2 + 2) == 4


@pytest.mark.parametrize("int1, int2", [(3, 3), (4, 4), (5, 5), (6, 6)])
def test_substraction(int1, int2):
    """_summary_"""
    assert (int1 - (int2)) == 0


def test_db(db_conn):
    print(db_conn)


def get_os_user_lower():
    """Simple retrieval function.

    Returns lowercase USER or raises OSError.
    """
    username = os.getenv("USER")

    if username is None:
        raise OSError("USER environment is not set.")

    return username.lower()


def test_upper_to_lower(mock_env_user):
    assert get_os_user_lower() == "testinguser"


def test_raise_exception(mock_env_missing):
    with pytest.raises(OSError):
        _ = get_os_user_lower()
