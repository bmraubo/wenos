import json


class DataGatherer:
    api_keys = {}

    def __init__(self, api_key_file):
        self.api_keys = self.read_api_key_file(api_key_file)

    def read_api_key_file(self, api_key_file):
        with open(api_key_file, "r") as f:
            parsed_file = f.read()
            return json.loads(parsed_file)
