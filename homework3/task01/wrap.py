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


@Memoize
def foo(a, b):
    return a * b
