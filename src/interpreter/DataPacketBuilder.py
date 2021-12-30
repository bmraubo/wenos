import os.path
import json


class DataPacketBuilder:
    def __init__(self):
        self.data = self.create_data_packet_template()

    def create_data_packet_template(self):
        with open(
            os.path.join("src", "interpreter", "data_packet_template.json"), "r"
        ) as f:
            return json.loads(f.read())

    def set_data_timestamp(self, datetime: str):
        self.data["data_timestamp"] = datetime

    def set_current_weather(self, data_type: str, data_value):
        self.data["current"][data_type] = data_value

    def set_hourly_weather(self, hour: str, data_type: str, data_value):
        self.data["hourly"][hour][data_type] = data_value

    def add_weather_alert(self, alert: dict):
        self.data["alerts"].append(alert)

    def generate_data_packet(self):
        return self.data
