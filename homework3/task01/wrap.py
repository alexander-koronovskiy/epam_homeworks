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


def memoize_func(f):
    memo = dict()

    def func(*args):

        print(f"Run with args={args}, memo={memo}")

        if args not in memo:
            memo[args] = f(*args)
        return memo[args]

    return func


@memoize_func
def func(a, b):
    return a ** b


func(3, 5)
func(3, 4)
func(3, 2)
func(3, 6)
func(3, 4)
func(3, 5)
