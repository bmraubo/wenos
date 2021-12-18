import pytest
from src.data_gatherer.data_gatherer import DataGatherer


def test_read_api_keys():
    test_file = "tests/test_api_key.json"

    test_gatherer = DataGatherer(test_file)

    expected_api_keys = {
        "service": "a service",
        "url": "www.a-url.interwebs",
        "api_key": "aNAPiK3y",
    }

    assert test_gatherer.api_keys == expected_api_keys
