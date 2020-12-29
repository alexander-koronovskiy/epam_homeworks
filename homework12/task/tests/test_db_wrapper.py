from task.db_handler import TableHandle

presidents = TableHandle("example.sqlite", "presidents")


def test_len():
    """
    test len protocol realisation at db wrapper class
    """
    assert len(presidents) == 3


def test_name():
    """
    test collection realisation at db wrapper class
    """
    assert dict(presidents["Yeltsin"])


def test_col():
    """
    test iter protocol at db wrapper class
    """
    for president in presidents:
        assert president["name"]


def test_contains():
    """
    test contains protocol at db wrapper class
    """
    assert "Gorbachev" not in presidents
