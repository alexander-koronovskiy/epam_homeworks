import sys


def my_precious_logger(s: str):
    """
    function that will receive a string and write it to stderr
    if line starts with "error" and to the stdout otherwise.
    """
    if s[:5] == "error":
        print(s, file=sys.stderr, end="")
    else:
        print(s, file=sys.stdout, end="")
