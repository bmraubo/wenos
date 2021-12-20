from src.weather_service import WeatherService
from OpenWeatherMock import Probe

# Read API Key File
def test_read_api_keys():
    test_file = "tests/test_api_key.json"

    weather_service = WeatherService.WeatherService()
    weather_service.read_api_key_file(test_file)

    expected_api_keys = {"service": "aNAPiK3y"}

    assert weather_service.api_keys == expected_api_keys


def test_set_user_location():
    test_file = "tests/test_api_key.json"
    user_location = (0.02, 0.01)

    weather_service = WeatherService.WeatherService()
    weather_service.read_api_key_file(test_file)
    weather_service.set_user_location(user_location)

    assert weather_service.user_location == user_location


def test_prepare_probe():
    test_file = "tests/test_api_key.json"
    user_location = (0.02, 0.01)

    weather_service = WeatherService.WeatherService()
    weather_service.read_api_key_file(test_file)
    weather_service.set_user_location(user_location)

    probe = Probe()
    weather_service.prepare_probe(probe)

    assert weather_service.probe.api_key == "aNAPiK3y"
    assert weather_service.probe.user_location == user_location


def test_get_weather_data():
    test_file = "tests/test_api_key.json"
    user_location = (0.02, 0.01)

    weather_service = WeatherService.WeatherService()
    weather_service.read_api_key_file(test_file)
    weather_service.set_user_location(user_location)

    probe = Probe()
    weather_service.prepare_probe(probe)
    weather_service.get_weather_data()

    assert type(weather_service.weather_data) == dict
