import os
import re
from typing import List
from keyword_script import KeywordScript



def is_subpath(path_a: str, path_b: str) -> bool:
    abs_path_a = os.path.abspath(path_a)
    abs_path_b = os.path.abspath(path_b)
    return os.path.commonpath([abs_path_a, abs_path_b]) == abs_path_a


def is_destination_path_valid(root_code_path: str, destionation_path: str) -> bool:
    if not is_subpath(root_code_path, destionation_path):
        print("Error: The destination path is not a subpath of the root code path.")
        print(f"    Destination path: {destionation_path}")
        print(f"    Root code path: {root_code_path}")
        return False
    return True


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


def get_root_code_path(destination_path: str, source_code_path_segment: str) -> str:
    pos = destination_path.find(source_code_path_segment)
    if pos != -1:
        return destination_path[:pos + len(source_code_path_segment)]
    return None