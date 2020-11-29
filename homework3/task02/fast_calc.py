"""
Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
"""
import hashlib
import random
import struct
import time
from multiprocessing import Pool, cpu_count
from threading import Thread
from timeit import default_timer as timer


class MyThread(Thread):
    """
    A threading example
    """

    summ = 0

    def __init__(self, name):
        """Thread initialization"""
        Thread.__init__(self)
        self.name = name

    def run(self):
        """thread start"""
        self.summ += slow_calculate(self.name)


def create_threads(n: int):
    """
    threads group creation
    """
    for i in range(n):
        my_thread = MyThread(i)
        my_thread.start()


def pm_calc(times=50):
    """
    New calculation function
    """
    start = timer()
    print(f"starting computations on {cpu_count()} cores")
    values = range(times)

    with Pool() as pool:
        res = pool.map(slow_calculate, values)

    sum(res)
    end = timer()
    return int(end - start)


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))
