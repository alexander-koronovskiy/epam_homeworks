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
    stat = False
    count = 1  # 'magic' number handler helper

    # file existing
    if os.path.isfile(path):
        with open(path) as f:

            # buffer creation
            while True:
                count += 1
                buf = f.read(16)
                if not buf:
                    break

                # 'magic' number handle
                while "\n" not in buf:
                    # first entrance handler
                    if not count == 1:
                        break
                    else:
                        # step-by-step handle, to avoid too multilevel nesting
                        if not (buf[0] and buf[0].isalnum()):
                            break
                        if int(buf[0]) not in [1, 2]:
                            break
                        if not (buf[1] and buf[1] == "."):
                            break
                        if not buf[2:15].isalnum():
                            break
                    if not buf.isalnum():
                        break
                    else:
                        stat = True

    if not stat:
        stat = ValueError
    return stat
