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
from collections import OrderedDict


def cache(times=10):
    def decorator(f):
        memo = OrderedDict()

        def wrapper(*args):
            if len(memo) == times:
                memo.popitem(last=False)
            memo[args] = f(*args)
            return {k: v for k, v in zip(memo.keys(), memo.values())}

        return wrapper

    return decorator
