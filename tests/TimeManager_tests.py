from datetime import datetime, time
from src.director import TimeManager


def test_time_check():
    current_time = datetime.now().strftime("%H:%M")

    time_manager = TimeManager.TimeManager()

    assert time_manager.check_time() == current_time


def test_time_manager_add_notification_time():
    notification_time = "01:01"

    time_manager = TimeManager.TimeManager()
    time_manager.add_notification_time(notification_time)

    assert time_manager.notification_times[0] == notification_time


def test_notification_time():
    current_time = "00:00"

    time_manager = TimeManager.TimeManager()
    time_manager.add_notification_time(current_time)

    assert time_manager.notification_time(current_time) == True


def test_alert_check_time():
    current_time = "00:00"

    time_manager = TimeManager.TimeManager()

    assert time_manager.alert_check_time(current_time) == True
