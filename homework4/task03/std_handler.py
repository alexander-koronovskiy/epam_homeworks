import sys


def errprint(*args, **kwargs):
    print(*args, file=sys.stderr, end="", **kwargs)
