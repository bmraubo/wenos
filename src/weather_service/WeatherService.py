import json


class WeatherService:
    api_keys = {}
    user_location = ()
    probe = None
    weather_data = None

    def read_api_key_file(self, api_key_file):
        with open(api_key_file, "r") as f:
            parsed_file = f.read()
            self.api_keys = json.loads(parsed_file)

    def set_user_location(self, user_location):
        self.user_location = user_location

    def prepare_probe(self, probe):
        probe.set_api_key(self.api_keys[probe.service])
        probe.set_user_location(self.user_location)
        self.probe = probe

    def get_weather_data(self):
        self.weather_data = self.probe.get_weather_data()
