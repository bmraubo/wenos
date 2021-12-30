import pytest
from src.interpreter.DataPacket import DataPacket
from src.interpreter.DataPacketBuilder import DataPacketBuilder


def test_create_data_packet():
    data_packet_builder = DataPacketBuilder()
    data_packet = DataPacket(data_packet_builder)

    assert data_packet.builder != None
