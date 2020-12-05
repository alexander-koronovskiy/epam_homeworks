from task03.tick_tack_toe import tic_tac_toe_checker


def test_unfinished():
    assert (
        tic_tac_toe_checker([["", "", "0"], ["", "x", "0"], ["x", "0", "x"]])
        == "unfinished"
    )


def test_win():
    assert (
        tic_tac_toe_checker([["", "", "0"], ["", "0", "0"], ["x", "x", "x"]]) == "x win"
    )
