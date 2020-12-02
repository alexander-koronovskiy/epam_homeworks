"""
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run
"""
import os


def read_magic_number(path: str) -> bool:
    """
    If first line is a number return true if number in an interval [1, 3) and false otherwise.
    :param path: file path
    :return: True or value_error
    """
    if not os.path.isfile(path):
        raise ValueError
    else:
        with open(path) as f:
            wonder_sym = f.read(1)
            if not wonder_sym.isalnum():
                raise ValueError
            wonder_sym = f.read(1)
            if wonder_sym.isspace():
                return True
            if not wonder_sym == ".":
                raise ValueError
            while True:
                wonder_sym = f.read(1)
                if wonder_sym.isspace():
                    break
                if not wonder_sym.isalnum():
                    raise ValueError

    return True


# read_magic_number('task_description.txt')
