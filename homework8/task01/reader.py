from typing import Dict


def content_reader(file: str) -> Dict:
    stringList = {}
    with open(file) as f:
        for line in f:
            key, value = line[:-1].split("=")
            stringList[key] = value
        return stringList
