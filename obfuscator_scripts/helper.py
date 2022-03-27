# imports here
import os
import random
import string
from contextlib import contextmanager
from typing import List


def get_lines_from_file(file_name: str) -> List[str]:
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            # Return a list with the non blank lines contained in the file.
            # https://stackoverflow.com/questions/4842057/easiest-way-to-ignore-blank-lines-when-reading-a-file-in-python
            return list(filter(None, (line.rstrip() for line in file)))
    except Exception as e:
        print('Error during reading file "{0}": {1}'.format(file_name, e))
        raise


def get_nop_op_codes() -> List[str]:
    return get_lines_from_file(
        os.path.join(os.path.dirname(__file__), "resources", "nop_op_codes.txt")
    )

def get_random_string(length: int) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))
    
@contextmanager
def inplace_edit_file(file_name: str):
    """
    Allow for a file to be replaced with new content.
    Yield a tuple of (readable, writable) file objects, where writable replaces
    readable. If an exception occurs, the old file is restored, removing the
    written data.
    """

    backup_file_name = "{0}{1}{2}".format(file_name, os.extsep, "bak")

    try:
        os.unlink(backup_file_name)
    except OSError:
        pass
    os.rename(file_name, backup_file_name)

    readable = open(backup_file_name, "r", encoding="utf-8")
    try:
        perm = os.fstat(readable.fileno()).st_mode
    except OSError:
        writable = open(file_name, "w", encoding="utf-8", newline="")
    else:
        os_mode = os.O_CREAT | os.O_WRONLY | os.O_TRUNC
        if hasattr(os, "O_BINARY"):
            os_mode |= os.O_BINARY
        fd = os.open(file_name, os_mode, perm)
        writable = open(fd, "w", encoding="utf-8", newline="")
        try:
            if hasattr(os, "chmod"):
                os.chmod(file_name, perm)
        except OSError:
            pass
    try:
        yield readable, writable
    except Exception as e:
        try:
            os.unlink(file_name)
        except OSError:
            pass
        os.rename(backup_file_name, file_name)

        print(
            'Error during inplace editing file "{0}": {1}'.format(file_name, e)
        )
        raise
    finally:
        readable.close()
        writable.close()
        try:
            os.unlink(backup_file_name)
        except OSError:
            pass

def get_random_int(min_int: int, max_int: int) -> int:
    return random.randint(min_int, max_int)


def get_junk_method(file_name: str):  # Return the junk method
    try:

        new_file_name = os.path.join(os.path.dirname(__file__), "resources", file_name)
        with open(new_file_name, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print('Error during reading file "{0}": {1}'.format(file_name, e))
        raise