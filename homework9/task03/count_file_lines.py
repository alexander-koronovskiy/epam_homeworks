"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    os.chdir(dir_path)
    count = 0
    for item in Path(".").glob("*"):
        if item.is_file() and str(item)[-len(file_extension) :] == file_extension:
            # counting lines
            with open(item) as f:
                size = sum(1 for _ in f)
            count += size
    return count
