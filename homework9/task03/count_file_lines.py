"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
"""

# задача 2 посчитать количество строк в них

import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    pass


os.chdir("D:\dev\epam courses\homework9")

count = 0
for item in Path(".").glob("*"):
    if item.is_file() and str(item)[-3:] == "txt":
        count += 1
print(count)
