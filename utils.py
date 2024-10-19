import os

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