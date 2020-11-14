"""
Задача готова, если:
  - функция создана +
  - функция правильно отформатирована +
  - функция имеет положительные и отрицательные тесты +
  - все временные файлы удаляются после пробного запуска
"""
import os


def read_magic_number(path: str) -> bool:
    """
    If first line is a number return true if number in an interval [1, 3) and false otherwise.
    :param path: file path
    :return: True or value_error
    """
    stat = False
    count = 0
    if os.path.isfile(path):
        with open(path) as f:
            for i in f.readline():
                count += 1
                if i.isalnum():
                    stat = int(i) in [1, 2]
                if count > 2:
                    stat = False
                    break
    if not stat:
        stat = ValueError
    return stat
