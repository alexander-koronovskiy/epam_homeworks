from task01.handler_file import *

for word in word_stream(file="task01/texts/simple_data.txt", encoding="utf-8"):
    print(word)  # 0
print(get_longest_diverse_words("task01/texts/simple_data.txt", encoding="utf-8"))  # 1
print(get_rarest_char("task01/texts/simple_data.txt", encoding="utf-8"))  # 2
print(count_punctuation_chars("task01/texts/simple_data.txt", encoding="utf-8"))  # 3
print(count_non_ascii_chars("task01/texts/data.txt", encoding="unicode-escape"))  # 4
print(
    get_most_common_non_ascii_char("task01/texts/data.txt", encoding="unicode-escape")
)  # 5
