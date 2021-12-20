from OpenWeatherMock import Probe


def test_set_api_key():
    probe = Probe()
    probe.set_api_key("aaaa")

    assert probe.api_key == "aaaa"


def test_set_user_location():
    user_location = (0.00, 0.00)

    probe = Probe()
    probe.set_user_location(user_location)

    assert probe.user_location == user_location


def test_create_request_url():
    api_key = "aaaa"
    lat_lon = (0.02, 0.01)

    probe = Probe()
    probe.set_api_key(api_key)
    probe.set_user_location(lat_lon)
    probe.create_request_url()

    expected_url = "https://api.openweathermap.org/data/2.5/onecall?lat=0.02&lon=0.01&exclude=minutely&appid=aaaa&units=metric"

    assert probe.request_url == expected_url


def test_make_request():
    api_key = "aaaa"
    lat_lon = (0.02, 0.01)

    probe = Probe()
    probe.set_api_key(api_key)
    probe.set_user_location(lat_lon)
    probe.create_request_url()
    probe.make_request()

    assert probe.request_sent == True
    assert type(probe.response) == dict
