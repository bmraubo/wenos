from datetime import datetime
from src.director import Director


def test_director_time_check():
    current_time = datetime.now().strftime("%H:%M")

    director = Director.Director()

    assert director.check_time() == current_time
