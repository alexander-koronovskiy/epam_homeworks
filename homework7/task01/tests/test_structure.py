"""
Test cases

case 1. sought-for value in dict values - example_tree
case 2. sought-for value in dict keys - find_me
case 3. empty example - empty tree

Check
 - value assertion
 - entry assertion for helper class
"""

from task01.structure_finder import find_occurrences

# case 1
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

# case 2
find_me = {"Me": {"a": 2, "Me": "bop"}, "z": {"Me": 4}}

# case 3
empty_tree = {}


def test_value_1():
    """
    it's lector's example, modified by me,
    i'm add in example a tuple, not change the the general value of 'RED'
    Main idea it's sought-for in dict values
    """
    assert find_occurrences(example_tree, "RED") == 6


def test_value_2():
    """
    My example
    sought-for value in dict keys
    """
    assert find_occurrences(find_me, "Me") == 3


def test_value_3():
    """
    My example of empty tree
    """
    assert not find_occurrences(empty_tree, "Default")
