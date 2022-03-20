import itertools
import os
import random
import re
import string
from contextlib import contextmanager
from hashlib import md5, sha256
from typing import List


def get_non_empty_lines_from_file(file_name: str) -> List[str]:
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            # Return a list with the non blank lines contained in the file.
            return list(filter(None, (line.rstrip() for line in file)))
    except Exception as e:
        print('Error during reading file "{0}": {1}'.format(file_name, e))
        raise


def get_nop_valid_op_codes() -> List[str]:
    return get_non_empty_lines_from_file(
        os.path.join(os.path.dirname(__file__), "resources", "op_code_for_nop.txt")
    )


def get_random_int(min_int: int, max_int: int) -> int:
    return random.randint(min_int, max_int)

