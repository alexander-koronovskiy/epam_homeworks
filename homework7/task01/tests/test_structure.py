"""
Test cases

case 1.


"""
from task01.structure_finder import some_useful_func

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}

empty_element = {}
lst = {"A": ["1", "2", {"3": "RED"}], "B": ["2"], "C": ["1", "2"]}
findMe = {"Me": {"a": 2, "Me": "bop"}, "z": {"Me": 4}}


def keyHole(k2b, o):

    if isinstance(o, dict):
        for k, v in o.items():
            if k == k2b and not hasattr(v, "__iter__"):
                yield v
            else:
                for r in keyHole(k2b, v):
                    yield r

    """
    elif hasattr(o, '__iter__'):
    for r in [keyHole(k2b, i) for i in o]:
        for item in r:
            yield item
    """

    return


print([x for x in keyHole("Me", findMe)])
print(some_useful_func(lst))
