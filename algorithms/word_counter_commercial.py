from collections import Counter


def word_counter(file):
    words = []
    with open(file) as f:
        for line in f.readlines():
            words.extend(line.lower().split(' '))
    return Counter(words).most_common(100)


for res in word_counter('assets/doc.txt'):
    print(res)
