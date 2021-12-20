import requests
import json


class Probe:
    service = "open_weather"
    request_url = ""
    units = "metric"
    response = {}
    api_key = ""
    user_location = ()

    def get_weather_data(self):
        self.response = self.make_request()
        return self.response

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_user_location(self, user_location):
        self.user_location = user_location

    def create_request_url(self):
        self.request_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={self.user_location[0]}&lon={self.user_location[1]}&exclude=minutely&appid={self.api_key}&units={self.units}"

    def make_request(self):
        return requests.post(self.request_url)
