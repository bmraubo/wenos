from datetime import datetime


class Director:
    def check_time(self):
        return datetime.now().strftime("%H:%M")
