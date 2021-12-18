from src.weather_service import OpenWeatherProbe
from src.weather_service import DataGatherer
import requests
import os.path


def test_create_request_url():
    api_key = "aaaa"
    lat_lon = (0.02, 0.01)

    weather_probe = OpenWeatherProbe.Probe(api_key, lat_lon)

    expected_url = "https://api.openweathermap.org/data/2.5/onecall?lat=0.02&lon=0.01&exclude=minutely&appid=aaaa&units=metric"

    assert weather_probe.request_url == expected_url


def test_make_request():
    data_gatherer = DataGatherer.DataGatherer(os.path.join("src", "api_keys.json"))
    api_key = data_gatherer.api_keys["open_weather"]["api_key"]
    lat_lon = (51.026376, -1.315293)

    probe = OpenWeatherProbe.Probe(api_key, lat_lon)
    response = probe.make_request()

    assert response.status_code == 200
