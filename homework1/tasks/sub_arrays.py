"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


# разбить на подмассивы, сложить, отсортировать
def find_maximal_sub_array_sum(nums: List[int], k: int) -> int:
    s = []
    for i in range(len(nums)):
        s.append(sum(nums[i : i + k]))
    return max(s)


print(find_maximal_sub_array_sum([1, 3, -1, -3, 5, 3, 6, 7], k=3))
