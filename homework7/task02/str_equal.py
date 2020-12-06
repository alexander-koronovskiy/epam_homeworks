# Input:
s = "ab#c"
t = "ad#c"  # Output: True


def backspace_compare(first: str, second: str):
    return process_backspaces(first) == process_backspaces(second)


def process_backspaces(input_s: str):
    back_space = "#"
    # buffer
    output = input_s.split("#", maxsplit=-1)
    # найти первый
    return output


# examples
# 1 тестовые варианты из задания
# 2 aa###c и ###c


print(process_backspaces("aa###c"))
