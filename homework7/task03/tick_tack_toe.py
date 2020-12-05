from typing import List


def tic_tac_toe_checker(field: List[List]) -> str:
    if (
        (field[0][0] == "0" and field[0][1] == "0" and field[0][2] == "0")
        or (field[0][0] == "0" and field[1][0] == "0" and field[2][0] == "0")
        or (field[0][1] == "0" and field[1][1] == "0" and field[2][1] == "0")
        or (field[0][2] == "0" and field[1][2] == "0" and field[2][2] == "0")
        or (field[1][0] == "0" and field[1][1] == "0" and field[1][2] == "0")
        or (field[2][0] == "0" and field[2][1] == "0" and field[2][2] == "0")
        or (field[0][0] == "0" and field[1][1] == "0" and field[2][2] == "0")
        or (field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0")
    ):
        return "0 win"
    elif (
        (field[0][0] == "x" and field[0][1] == "x" and field[0][2] == "x")
        or (field[0][0] == "x" and field[1][0] == "x" and field[2][0] == "x")
        or (field[0][1] == "x" and field[1][1] == "x" and field[2][1] == "x")
        or (field[0][2] == "x" and field[1][2] == "x" and field[2][2] == "x")
        or (field[1][0] == "x" and field[1][1] == "x" and field[1][2] == "x")
        or (field[2][0] == "x" and field[2][1] == "x" and field[2][2] == "x")
        or (field[0][0] == "x" and field[1][1] == "x" and field[2][2] == "x")
        or (field[0][2] == "x" and field[1][1] == "x" and field[2][0] == "x")
    ):
        return "x win"
    else:
        return "unfinished"
