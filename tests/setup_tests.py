import pytest
from src import setup
from os import remove
from os.path import join


def test_file_exists():
    file_name = "test.json"

    assert setup.check_file(file_name) == False


def test_file_create():
    file_name = "test.json"

    setup.create_file(file_name)

    assert setup.check_file(file_name) == True
    remove(file_name)


def test_feature_create_files():
    test_files = [join("test.json"), join("test2.json")]

    setup.create_required_files(test_files)

    assert setup.check_file("test.json")
    assert setup.check_file("test2.json")

    remove("test.json")
    remove("test2.json")
