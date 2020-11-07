"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    n1, n2, n3, n4 = len(a), len(b), len(c), len(d)
    counter = 0
    for i in range(n1):
        for j in range(n2):
            for k in range(n3):
                for m in range(n4):
                    if a[i] + b[j] + c[k] + d[m] == 0:
                        counter += 1
    return counter
