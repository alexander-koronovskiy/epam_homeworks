"""
Декоратор instances_counter применяется к любому классу и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбрасывает счетчик экземпляров и возвращает значение до сброса
Имя декоратора и методов неизменно
"""
from task02.fast_calc import benchmark, slow_calculate


@benchmark
def total_sum(n):
    return sum([slow_calculate(i) for i in range(n)])


print(total_sum(5))  # распаралеллить вычисления
