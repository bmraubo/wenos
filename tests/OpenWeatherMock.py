import os.path
import json


class Probe:
    service = "service"
    request_url = ""
    units = "metric"
    response = {}
    api_key = ""
    user_location = ()

    # Mock variables
    response_stub = {}
    request_sent = False
    request_sent_to = ""

    def get_weather_data(self):
        self.response = self.make_request()
        return self.convert_weather_data_to_dict(self.response)

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_user_location(self, user_location):
        self.user_location = user_location

    def create_request_url(self):
        self.request_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={self.user_location[0]}&lon={self.user_location[1]}&exclude=minutely&appid={self.api_key}&units={self.units}"

    def make_request(self):
        self.request_sent = True
        self.request_sent_to = self.request_url
        return self.read_response_stub()

    def convert_weather_data_to_dict(self, weather_data_string):
        return json.loads(weather_data_string)

    # Mock methods
    def read_response_stub(self):
        with open(os.path.join("tests", "response_stub.json"), "r") as f:
            file_contents = f.read()
            return file_contents
