import requests


class Probe:
    request_url = ""
    units = "metric"
    response = {}

    def __init__(self, api_key, lat_lon):
        self.request_url = self.create_request_url(api_key, lat_lon)

    def create_request_url(self, api_key, lat_lon):
        return f"https://api.openweathermap.org/data/2.5/onecall?lat={lat_lon[0]}&lon={lat_lon[1]}&exclude=minutely&appid={api_key}&units={self.units}"

    def make_request(self):
        return requests.post(self.request_url)
