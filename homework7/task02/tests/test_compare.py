from task02.str_equal import backspace_compare, process_backspaces


def test_process_my() -> bool:
    """
    test working func process
    example with no back spaces

    case: a == a
    case: abc == abc
    """
    assert process_backspaces("a") == "a"
    assert process_backspaces("abc") == "abc"


def test_process_func() -> bool:
    """
    check it with back space
    case: ##aabbcc == aabbcc
    """
    assert process_backspaces("##aabbcc") == "aabbcc"


def test_compare_one() -> bool:
    """
    lect example 1
    :return: backspace_compare -> True
    """
    assert backspace_compare("ab#c", "ad#c")


def test_compare_two() -> bool:
    """
    lect example 2
    :return: backspace_compare -> True
    """
    assert process_backspaces("a##c") == "c"
    assert process_backspaces("#a#c") == "c"


def test_compare_three() -> bool:
    """
    my example, cases

    aabb##cc == aacc
    aaccbb## == aacc
    :return backspace_compare -> True
    """
    assert backspace_compare("aabb##cc", "aaccbb##")
