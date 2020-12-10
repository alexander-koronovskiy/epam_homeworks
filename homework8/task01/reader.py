from typing import List


def word_reader(file: str, encoding: str = "utf-8") -> List:
    """
    Buffer the file, then handle this to word generator
    """
    with open(file, encoding=encoding) as f:
        while True:

            # buffer creation
            buf = f.read(65536).lower()
            if not buf:
                break

            # word boundary check
            while not str.isspace(buf[-1]):
                ch = f.read(1)
                if not ch:
                    break
                buf += ch

            # work with buffer content
            record = ""
            words = []

            # words handling
            for symbol in buf:

                # divided by word
                if symbol == "=":
                    words.extend(record.split())
                    words.append(symbol)
                    record = ""
                else:
                    record += symbol

            # EOF handling
            words.extend(record.split())

            # word streaming
            return words
