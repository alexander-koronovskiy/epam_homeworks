from task01.handler_storage import KeyValueStorage


def test_content_exist():
    """
    check for return attribute
    check for return collection element

    check for saving value type
    check for attribute value priority
    """
    content = KeyValueStorage("key_storage.txt")
    assert content["name"] == "kek"
    assert content.power == 9001


def test_err():
    """
    numeric key error check
    """
    try:
        content = KeyValueStorage("invalid_storage.txt")
        test_val = content.name
    except ValueError:
        test_val = []
    assert not test_val
