from datetime import datetime
from src.director import Director


def test_director_time_check():
    current_time = datetime.now().strftime("%H:%M")

    director = Director.Director()

    assert director.check_time() == current_time


def test_director_add_notification_time():
    notification_time = "01:01"

    director = Director.Director()
    director.add_notification_time(notification_time)

    assert director.notification_times[0] == notification_time


def test_is_it_notification_time():
    notification_time = datetime.now().strftime("%H:%M")

    director = Director.Director()
    director.add_notification_time(notification_time)

    assert director.is_it_notification_time() == True
