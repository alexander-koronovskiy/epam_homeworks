def quick_sort(l: list):
    if not l:
        return []
    else:
        return (
            quick_sort([x for x in l if x < l[0]])
            + [l[0]]
            + quick_sort([x for x in l if x > l[0]])
        )


print(quick_sort([1, 8, 9, -10, 64]))
