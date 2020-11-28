class memoize(dict):
    """
    That's a memoizing function that works on functions, methods, or classes,
    and exposes the cache publicly.
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


@memoize
def foo(a, b):
    return a * b


foo(2, 4)
foo("hi", 3)
print(foo)
