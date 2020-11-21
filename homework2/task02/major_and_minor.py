"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from collections import Counter
from typing import List, Tuple


# first realisation
def major_and_minor_elem(inp: List) -> Tuple[int, int]:

    # using map in this code make O(n) complicity
    el_map = {}
    for el in inp:
        if el in el_map:
            el_map[el] += 1
        else:
            el_map[el] = 1

    el_sorted = sorted(el_map.items(), key=lambda item: item[1], reverse=True)
    return el_sorted[0][0], el_sorted[-1][0]


def quick_sort(l):
    if not l:
        return []
    else:
        return (
            quick_sort([x for x in l if x < l[0]])
            + [x for x in l if x == l[0]]
            + quick_sort([x for x in l if x > l[0]])
        )


# another realisation (earlier)
def major_and_minor_elem_0(inp: List) -> Tuple[int, int]:

    # init counter
    loc_storage = []
    result = []
    count = 1

    # check input data
    if inp:

        # O(n log n) sorted  + added memory
        for i in quick_sort(inp):

            # first occurrence calculation skip
            if not loc_storage:
                loc_storage.append(i)
                continue

            # occurrence calculation
            if loc_storage[-1] == i:
                count += 1
            else:
                result.append((loc_storage[-1], count))
                count = 1
            loc_storage.append(i)

        # last occurrence calculation
        result.append((loc_storage[-1], count))

    else:
        result = ()

    if result:
        el_sorted = sorted(result, key=lambda item: item[1], reverse=True)
        return el_sorted[0][0], el_sorted[-1][0]
    else:
        return result
