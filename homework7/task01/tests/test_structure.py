from task01.correction import count, count_2, flatten

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", ("list", {"of": "MY extensions"}), "RED", "valued"],
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


def test_example_1():
    """
    test corrected realisation at first way
    """
    assert count(flatten(example_tree), "RED") == 6


def test_example_2():
    """
    test corrected realisation at second way
    """
    assert count_2(example_tree, "RED") == 6
