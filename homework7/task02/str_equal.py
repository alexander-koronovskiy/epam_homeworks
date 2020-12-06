def backspace_compare(first: str, second: str) -> bool:
    return process_backspaces(first) == process_backspaces(second)


def process_backspaces(input_s: str) -> str:

    # example symbol of deletions
    back_space = "#"

    if input_s.find(back_space) == -1:
        # simple case for no deletions
        return input_s
    else:
        # handler
        output = input_s.split(back_space, maxsplit=-1)

        # we have a deletions at start of the output result
        if output:
            c = 0
            if not output[0]:
                while not output[c]:
                    c += 1
        output = output[c:]

    # case only one backspace
    if "" not in output:
        return "".join([i[:-1] for i in output[:-1]]) + str(output[-1])

    # more complicity cases
    else:
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
