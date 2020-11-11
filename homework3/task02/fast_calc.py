import hashlib
import random
import struct
import time
from threading import Thread


class MyThread(Thread):
    """
    A threading example
    """

    def __init__(self, name):
        """Thread initialization"""
        Thread.__init__(self)
        self.name = name

    def run(self):
        """thread start"""
        msg = self.name
        slow_calculate(msg)


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def create_threads(n: int):
    """
    threads group creation
    """
    for i in range(n):
        my_thread = MyThread(i)
        my_thread.start()
