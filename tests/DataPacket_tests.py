import pytest
from src.interpreter.DataPacket import DataPacket
from src.interpreter.DataPacketBuilder import DataPacketBuilder


def test_create_data_packet():
    data_packet_builder = DataPacketBuilder()
    data_packet = DataPacket(data_packet_builder)

    assert data_packet.builder != None


def test_add_current_data():
    current_data = {
        "time": "10:00",
        "sunrise": "09:00",
        "sunset": "17:00",
        "temp": 10,
        "feelslike": 20,
        "humidity": 10,
        "uvi": 10,
        "wind_speed": 0.9,
        "wind_gusts": 1.2,
        "weather": {"general": "raining", "description": "cats and dogs"},
    }

    data_packet_builder = DataPacketBuilder()
    data_packet = DataPacket(data_packet_builder)

    data_packet.add_current_weather(current_data)
    data_packet.generate_data_packet()

    assert data_packet.data["current"]["temp"] == 10
    assert data_packet.data["current"] == current_data
