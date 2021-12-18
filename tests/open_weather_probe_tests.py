from src.weather_service import OpenWeatherProbe


def test_create_request_url():
    api_key = "aaaa"
    lat_lon = (0.02, 0.01)

    weather_probe = OpenWeatherProbe.Probe(api_key, lat_lon)

    expected_url = (
        "https://api.openweathermap.org/data/2.5/onecall?lat=0.02&lon=0.01&appid=aaaa"
    )

    assert weather_probe.request_url == expected_url
