import pytest
from src import setup


def test_file_exists():
    file_name = "test.json"

    assert setup.check_file(file_name) == False


def test_file_create():
    file_name = "test.json"

    setup.create_file(file_name)

    assert setup.check_file(file_name) == True
