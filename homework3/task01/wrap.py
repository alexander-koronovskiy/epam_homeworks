"""
Example how it must works

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

f()
? 1
'1'
f()     # will remember previous value
'1'
f()     # but use it up to two times only
'1'
f()
? 2
'2'
"""


class Memoize(dict):
    """
    That's a memoizing function that works on functions, methods, or classes,
    and exposes the cache publicly.
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        if len(self) == 2:
            self.clear()
        self[key] = self.func(*key)
