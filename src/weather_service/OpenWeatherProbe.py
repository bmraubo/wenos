import requests
import json


class Probe:
    service = "open_weather"
    request_url = ""
    units = "metric"
    response = {}
    api_key = ""
    user_location = ()

    def get_weather_data(self, api_key, lat_lon):
        self.request_url = self.create_request_url(api_key, lat_lon)
        response = self.make_request()
        return self.convert_weather_data_to_dict(response.text)

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_user_location(self, user_location):
        self.user_location = user_location

    def create_request_url(self):
        self.request_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={self.user_location[0]}&lon={self.user_location[1]}&exclude=minutely&appid={self.api_key}&units={self.units}"

    def make_request(self):
        return requests.post(self.request_url)

    def convert_weather_data_to_dict(self, weather_data_string):
        return json.loads(weather_data_string)
