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


def decorator(f):
    memo = dict()

    def wrapper(*args):
        memo[args] = f(*args)
        print(f"Run with args={args}, memo={memo}")
        return memo[args]

    return wrapper


@decorator
def func(a, b):
    return a ** b


func(3, 5)
func(3, 4)
