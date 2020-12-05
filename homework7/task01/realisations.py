from task01.structure_finder import expand, traverse


def some_useful_func(lst):
    return ["{}.{}".format(key, val) for key, vals in lst.items() for val in vals]


def unpack(data):
    for k, v in data.items():
        if isinstance(v, dict):
            yield from unpack(v)
        else:
            yield v


def keyHole(k2b, o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == k2b and not hasattr(v, "__iter__"):
                yield v
            else:
                for r in keyHole(k2b, v):
                    yield r
    return


def traverse(d: Dict) -> Generator:
    for key, val in d.items():
        if isinstance(val, dict):
            yield from traverse(val)

        else:
            yield val


def expand(lst: List[List]) -> List:
    """
    expand list
    """
    total = []
    for element in lst:
        if isinstance(element, list):
            total.extend(expand(element))
        else:
            total.append(element)
    return total


print([list(expand(traverse(x))) for x in [...]])
