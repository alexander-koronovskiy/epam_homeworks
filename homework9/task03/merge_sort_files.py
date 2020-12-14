"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
"""

# задача 1 посчитать колиство .txt файлов
# задача 2 посчитать количество строк в них

import os
from pathlib import Path

os.chdir("D:\dev\epam courses\homework9")

print(len(list(Path(".").glob("*"))))
print(len(list(Path(".").glob("**/*"))))

for item in Path(".").glob("*"):
    if item.is_file():
        print(str(item), str(item.absolute()))
