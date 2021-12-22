from datetime import datetime
from src.director.TimeManager import TimeManager


class Director:
    time_manager = TimeManager()

    def add_notification_time(self, notification_time):
        self.time_manager.add_notification_time(notification_time)
