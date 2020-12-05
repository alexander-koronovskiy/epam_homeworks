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
