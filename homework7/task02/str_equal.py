# Input:
s = "ab#c"
t = "ad#c"  # Output: True


def backspace_compare(first: str, second: str):
    return process_backspaces(first) == process_backspaces(second)


def process_backspaces(input_s: str):

    # buffer_reader realize this, then handler

    # handler
    back_space = "#"

    # Test case a = a, abc == abc
    if input_s.find(back_space) == -1:
        return input_s

    # code for another test cases
    else:
        output = input_s.split(back_space, maxsplit=-1)

    # case only one backspace
    if "" not in output:
        return "".join([i[:-1] for i in output[:-1]]) + str(output[-1])

    # only many, complex
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


# test_compare_zero False
# comment: working func process with no back space
print("case: a == a", process_backspaces("a"))
print("case: abc == abc", process_backspaces("abc"))

# test_process_func_check_with_back_space
print("case: ##aabbcc == aabbcc", process_backspaces("##aabbcc"))


# test_compare_one lect example 1 True
print("case: ab#c == ac", process_backspaces("ab#c"))
print("case: ad#c == ac", process_backspaces("ad#c"))

# test_compare_two lect example 2 a moment of true
print("case: a##c == c", process_backspaces("a##c"))
print("case: #a#c == c", process_backspaces("#a#c"))

# test_compare_three my example
print("case: aabb##cc == aacc", process_backspaces("aabb##cc"))
print("case: aaccbb## == aacc", process_backspaces("aaccbb##"))
