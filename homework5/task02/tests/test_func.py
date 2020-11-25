from task02.funcs import *


def test_func():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"
    assert str(custom_sum.__original_func)[1:20] == "function custom_sum"
