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
