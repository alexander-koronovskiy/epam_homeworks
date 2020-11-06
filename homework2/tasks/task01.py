def check_power_of_2(a: int) -> bool:
    """
    program that checks a custom number for a power of 2
    :param a: number, that user wants to check
    :return: expected result
    """
    return a != 0 and a & (a - 1) == 0
