from datetime import datetime


class TimeManager:
    def __init__(self):
        self.notification_times = []
        self.alert_check_frequencies = {
            "hour": "00",
        }

    def check_time(self):
        return datetime.now().strftime("%H:%M")

    def add_notification_time(self, notification_time):
        self.notification_times.append(notification_time)

    def set_alert_check_frequency(self, alert_check_frequency):
        self.alert_check = alert_check_frequency

    def is_it_notification_time(self):
        current_time = self.check_time()
        return current_time in self.notification_times
