def backspace_compare(first: str, second: str) -> bool:
    return process_backspaces(first) == process_backspaces(second)


def process_backspaces(input_s: str) -> str:

    # buffer_reader realize this, then handler

    # handler
    back_space = "#"

    # Test case a = a, abc == abc
    if input_s.find(back_space) == -1:
        return input_s

    # code for another test cases
    else:
        output = input_s.split(back_space, maxsplit=-1)

    # case only one backspace ???
    if "" not in output:
        return "".join([i[:-1] for i in output[:-1]]) + str(output[-1])

    # only many, complex
    else:

        # complex_case_handler(output)

        buffer = ""
        count_del = 0

        for i in output[:-1]:
            if i:
                buffer += i
                count_del = 0
            else:
                if not count_del:
                    count_del += 1
                    buffer = buffer[:-1]
                buffer = buffer[:-1]

        return buffer + str(output[-1])
