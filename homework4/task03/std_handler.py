import sys


def errprint(s):
    if s[:5] == "error":
        print(s, file=sys.stderr, end="")
    else:
        print(s, file=sys.stdout, end="")
