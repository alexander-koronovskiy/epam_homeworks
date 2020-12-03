"""
This is the "example" module.
The example module supplies one function, factorial().  For example,
>>> fizzbuzz(5)
[1, 2, 'Fizz', 4, 'Buzz']

That is complete insturction to how testing launch:

- visit website https://www.python.org/
- click 'Download' for install latest python version
- find python.exe on 'downloads' in your computer
- click python.exe and install it with default setting
- use github functional for copy that code or
copy this example in .txt file and then rename doc as 'fizzbuzz.py'
- good! At this step you have file 'fizzbuzz.py' on your computer
- open your computer command line (Ctrl+Alt+T in Linux, win+r cmd in Windows)
- print command 'python fizzbuzz.py -v'
- Best wishes!
"""


def fizzbuzz(n):
    """Return the fizzbuzz sequiency of n, an exact integer >= 0.

    >>> fizzbuzz(6)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz']
    >>> fizzbuzz(15)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
    >>> fizzbuzz(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be > 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> fizzbuzz(10.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    It must also not be ridiculously large:
    >>> fizzbuzz(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math

    if not n > 0:
        raise ValueError("n must be > 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")

    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
            continue
        if i % 3 == 0:
            result.append("Fizz")
            continue
        if i % 5 == 0:
            result.append("Buzz")
            continue
        result.append(i)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
