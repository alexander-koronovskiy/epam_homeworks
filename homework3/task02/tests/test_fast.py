from task02.fast_calc import benchmark, slow_calculate


@benchmark
def total_sum(n):
    return sum([slow_calculate(i) for i in range(n)])


print(total_sum(3))
