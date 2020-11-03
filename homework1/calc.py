def check_power_of_2(a: int) -> bool:
    return bool(a & ((a & (a - 1)) == 0))