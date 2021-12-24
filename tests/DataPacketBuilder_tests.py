import pytest
import json
import os.path
from src.interpreter.DataPacketBuilder import DataPacketBuilder


def read_data_packet_template_file():
    with open(
        os.path.join("src", "interpreter", "data_packet_template.json"), "r"
    ) as f:
        return json.loads(f.read())


def test_create_data_packet_template():
    data_packet_template = read_data_packet_template_file()

    data_packet_builder = DataPacketBuilder()

    assert data_packet_builder.data != None
    assert len(data_packet_builder.data) != 0
    assert data_packet_builder.data["current"]["temp"] == 0
    assert data_packet_builder.data == data_packet_template


def test_set_current_weather():
    current_temp = 5
    current_sunset = "15:56"

    data_packet_builder = DataPacketBuilder()
    data_packet_builder.set_current_weather("temp", current_temp)
    data_packet_builder.set_current_weather("sunset", current_sunset)

    assert data_packet_builder.data["current"]["temp"] == 5
    assert data_packet_builder.data["current"]["sunset"] == current_sunset


def test_set_hourly_weather():
    hour = "+1"
    temp = 5

    data_packet_builder = DataPacketBuilder()
    data_packet_builder.set_hourly_weather(hour, "temp", temp)

    assert data_packet_builder.data["hourly"]["+1"]["temp"] == 5
