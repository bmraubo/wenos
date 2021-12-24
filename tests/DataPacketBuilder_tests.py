import pytest
import json
import os.path
from src.interpreter.DataPacketBuilder import DataPacketBuilder


def read_data_packet_template_file():
    with open(
        os.path.join("src", "interpreter", "data_packet_template.json"), "r"
    ) as f:
        return json.loads(f.read)


def test_create_data_packet_template():
    data_packet_template = read_data_packet_template_file

    data_packet_builder = DataPacketBuilder()

    assert data_packet_builder.data != None
    assert len(data_packet_builder.data) != 0
    assert data_packet_builder.data["current"]["temp"] == 0
