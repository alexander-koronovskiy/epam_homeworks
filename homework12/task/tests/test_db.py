from task.myfiles import get_deadline


def get_deadline():
    assert str(get_deadline(3).year) == "2021"
