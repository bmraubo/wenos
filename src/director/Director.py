from datetime import datetime
from time import sleep
from src.director.TimeManager import TimeManager


class Director:
    def __init__(self):
        self.time_manager = TimeManager()

    def add_notification_time(self, notification_time):
        self.time_manager.add_notification_time(notification_time)

    def start(self):
        while True:
            current_time = datetime.now().strftime("%H:%M")
            if self.time_manager.notification_time(current_time):
                # Update Weather Data
                # Send weather data to Interpreter
                # Send Data Packet to Composer to create Notification Email
                # Send Email
                pass
            if self.time_manager.alert_check_time(current_time):
                # Update Weather Data
                # Send weather Data to Interpreter
                # Check Weather conditions
                # if weather conditions are good, pass
                # if specified weather conditions are met, send alert notification
                # Send Data Packet to Composer to create Alert Email
                # Send Email
                pass
            sleep(60)
