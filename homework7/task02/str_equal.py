# Input:
s = "ab#c"
t = "ad#c"  # Output: True


def backspace_compare(first: str, second: str):
    return process_backspaces(first) == process_backspaces(second)


def process_backspaces(input_s: str):

    # buffer_reader realize this, then handler

    back_space = "#"
    buffer = ""

    output = input_s.split(back_space, maxsplit=-1)

    for i in output:

        if i:
            buffer += i
            count = 0
        else:
            buffer = buffer[:-1]
            if not count:
                count += 1
                buffer = buffer[:-1]

    return output, buffer


# Test cases
# abc = abc
# ab#c = ac
# ab#c# = a


print("case: abc", process_backspaces("abc"))
print("case: ab#c is ac", process_backspaces("ab#c"))
