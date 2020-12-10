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


# stderr test for numerical key
