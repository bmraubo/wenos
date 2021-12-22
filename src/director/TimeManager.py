from datetime import datetime


class TimeManager:
    def __init__(self):
        self.notification_times = []
        self.alert_check = ["00"]

    def check_time(self):
        return datetime.now().strftime("%H:%M")

    def add_notification_time(self, notification_time):
        self.notification_times.append(notification_time)

    def add_alert_check_frequency(self, alert_check_frequency):
        self.alert_check.append(alert_check_frequency)

    def notification_time(self, current_time):
        return current_time in self.notification_times

    def alert_check_time(self, current_time):
        return current_time[3:] in self.alert_check
