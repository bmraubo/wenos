from datetime import datetime


class Director:
    notification_times = []

    def check_time(self):
        return datetime.now().strftime("%H:%M")

    def add_notification_time(self, notification_time):
        self.notification_times.append(notification_time)

    def is_it_notification_time(self):
        current_time = self.check_time()
        return current_time in self.notification_times

    def time_manager(self):
        while True:
            if self.is_it_notification_time():
                # update the weather data
                # send out an update email
                pass
            else:
                pass
