import os
import re
from fs_node import FSNode
from constants import *


def create_file_or_directory(base_path: str, node: FSNode, prefix: str, module_code_path: str):
    path = os.path.join(
        base_path, 
        node.name
            .replace(NAME_PREFIX, prefix.capitalize())
            .replace(NAME_PREFIX_LOWERCASE, prefix.lower())
    )
    
    if node.is_file:
        _create_file(path, module_code_path, node.template_file, prefix)
    else:
        _create_directory(path)
        for sub_node in node.sub_nodes:
            create_file_or_directory(path, sub_node, prefix, module_code_path)

def _create_file(file_path: str, module_code_path: str, template_file: str = None, prefix: str = None) -> bool:
    """Creates a file at the given path using a template."""
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                if template_file and prefix:
                    try:
                        with open(os.path.join(TEMPLATE_DIRECTORY, template_file), 'r') as template:
                            content = template.read()
                            package_name = _path_to_package(os.path.dirname(file_path), module_code_path)
                            content = _replace_case_insensitive(content, TEMPLATE_PREFIX, prefix)
                            content = content.replace(PACKAGE_NAME_KEYWORD, package_name)
                        file.write(content)
                    except FileNotFoundError:
                        print(f"Template file not found: {template_file}. Creating an empty file instead.")
                        file.write("")  # Fallback to creating an empty file
                else:
                    file.write("")  # Create an empty file
            print(f"File created: {file_path}")
            return True
        except IOError as e:
            print(f"Failed to create file: {file_path}. Error: {e}")
            return False
    else:
        print(f"File already exists: {file_path}")
        return False

def _create_directory(path: str) -> bool:
    """Creates a directory at the specified path."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
        return True
    else:
        print(f"Directory already exists: {path}")
        return False

def _replace_case_insensitive(text, old, new):
    """
    Replace the text keeping the original case.
    """
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

def _path_to_package(path: str, project_root: str) -> str:
    """Convert a file path to a package string."""
    relative_path = os.path.relpath(path, project_root)
    return relative_path.replace(os.sep, '.')