import os
import re
from typing import List
from keyword_script import KeywordScript
from config import SOURCE_PATH_CHUNK, TEST_PATH_CHUNK


def is_subpath(path_a: str, path_b: str) -> bool:
    abs_path_a = os.path.abspath(path_a)
    abs_path_b = os.path.abspath(path_b)
    return os.path.commonpath([abs_path_a, abs_path_b]) == abs_path_a


def print_indented(message: str, depth: int = 0):
    identation = get_indentation(depth)
    print(f"{identation}{message}")


def get_indentation(depth: int) -> str:
    indentation = ""
    for _ in range(depth):
        indentation += "    "
    return indentation


def replace_case_insensitive(text: str, old: str, new: str) -> str:
    def replace(match):
        matched_text = match.group()
        if matched_text.islower():
            return new.lower()
        elif matched_text.isupper():
            return new.upper()
        elif matched_text[0].isupper():
            return new.capitalize()
        else:
            return new

    pattern = re.escape(old)
    return re.sub(pattern, replace, text, flags=re.IGNORECASE)


def replace_keywords(text: str, keywords: List[KeywordScript]) -> str:
    for keyword in keywords:
        text = replace_case_insensitive(text, keyword.keyword, keyword.replacement)
    return text


def get_path_until_chunk(full_path: str, chunk: str) -> str:
    pos = full_path.find(chunk)
    if pos != -1:
        return full_path[:pos + len(chunk)]
    return None


def relative_path_to_package(path: str, base_path: str) -> str:
    if not is_subpath(base_path, path):
        return ""

    if os.path.isfile(path):
        path = os.path.dirname(path)
    relative_path = os.path.relpath(path, base_path)
    return relative_path.replace(os.sep, '.')



def get_package_of_path(path: str):
    """
    Retrieves the package for the current directory based on the given path.

    Assumes a structure similar to Java and Kotlin, where source code is in 
    'src/main/java'. It's crucial to consider the difference between the current 
    directory and this base directory. Not sure if this will work well in other 
    languages.
    """
    root_code_path = get_path_until_chunk(path, SOURCE_PATH_CHUNK)
    return relative_path_to_package(path, root_code_path)



def get_test_path_from_source_path(source_path: str) -> str:
    """
    Converts a source code path to a test path for Java/Kotlin projects.

    Assumes a typical 'src/main/java' and 'src/test/java' directory structure.
    Behavior may vary for other languages with different conventions.
    """
    return source_path.replace(SOURCE_PATH_CHUNK, TEST_PATH_CHUNK)


def read_lines(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return file.readlines()

def write_lines(file_path: str, lines: list):
    with open(file_path, 'w') as file:
        file.writelines(lines)
