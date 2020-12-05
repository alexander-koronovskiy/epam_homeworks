"""
Test cases

case 1. sought-for value in value // lector's example, modified with tuple - example tree
case 2. empty example - empty tree
case 3. sought-for value in key - find_me

Check
 - в предварительной функции нет вложенных словарей
 - обработка пустого результата
 - поиск идет как по ключам, так и по значениям

"""
from task01.structure_finder import Counts

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
empty_tree = {}

# case 3
find_me = {"Me": {"a": 2, "Me": "bop"}, "z": {"Me": 4}}


print(Counts().recursive(example_tree))
