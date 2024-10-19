import os
import re


def is_subpath(path_a: str, path_b: str) -> bool:
    abs_path_a = os.path.abspath(path_a)
    abs_path_b = os.path.abspath(path_b)
    return os.path.commonpath([abs_path_a, abs_path_b]) == abs_path_a


def is_destination_path_valid(root_code_path: str, current_path: str) -> bool:
    if not is_subpath(root_code_path, current_path):
        print("Error: The destination path is not a subpath of the root code path.")
        print(f"    Destination path: {current_path}")
        print(f"    Root code path: {root_code_path}")
        return False
    return True


def get_root_code_path(root_path: str, module: str, code_path: str) -> str:
    return os.path.join(root_path, module, code_path)


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
