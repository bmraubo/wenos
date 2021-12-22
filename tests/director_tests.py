from src.director.Director import Director


def test_add_notification_time():
    notification_time = "00:01"

    director = Director()
    director.add_notification_time(notification_time)

    assert director.time_manager.notification_times[0] == notification_time
