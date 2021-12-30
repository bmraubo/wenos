class DataPacket:
    def __init__(self, data_packet_builder):
        self.builder = data_packet_builder

    def add_current_weather(self, current_weather):
        for key, value in current_weather.items():
            self.builder.set_current_weather(key, value)

    def generate_data_packet(self):
        self.data = self.builder.generate_data_packet()
