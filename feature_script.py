import os
import re
from fs_node import FSNode
from constants import *

def check_directory(base_path: str, node: FSNode, prefix: str) -> bool:
    if node.is_file or node.optional:
        return True

    path = _get_node_path(base_path, node, prefix)
    if not os.path.exists(path):
        return False
    
    for sub_node in node.sub_nodes:
        if not check_directory(path, sub_node, prefix):
            return False
            
    return True



def create_file_or_directory(base_path: str, node: FSNode, prefix: str, module_code_path: str, depth: int = 0):
    """
    Creates a file or directory based on the provided FSNode information.

    Args:
        base_path: The base path where the file or directory will be created. (str)
        node: An FSNode object representing the file or directory structure. (FSNode)
        prefix: A prefix to be applied to the node name. (str)
        module_code_path: The path to the module code directory. (str)
    """

    path = _get_node_path(base_path, node, prefix)

    try:
        if node.is_file:
            _create_file(path, module_code_path, node.template_file, prefix, depth)
        else:
            _create_directory(path, depth)
            for sub_node in node.sub_nodes:
                create_file_or_directory(path, sub_node, prefix, module_code_path, depth+1)
    except OSError as e:
        print(f"Error creating file or directory: {e}")

def _get_node_path(base_path: str, node: FSNode, prefix: str) -> str:
    return os.path.join(
        base_path,
        node.name
            .replace(NAME_PREFIX, prefix.capitalize())
            .replace(NAME_PREFIX_LOWERCASE, prefix.lower())
    )


def _create_file(file_path: str, module_code_path: str, template_file: str = None, prefix: str = None, depth: int = 0) -> bool:
    """Creates a file at the given path using a template."""

    identation = _get_identation(depth)
    file_name = file_path.split("/")[-1]
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                if template_file and prefix:
                    try:
                        _add_content_from_template(file, template_file, file_path, module_code_path, prefix)
                    except FileNotFoundError:
                        print(f"{identation}Template file not found: {template_file}. Creating an empty file instead.")
                        file.write("")
                else:
                    file.write("")  # Create an empty file
            print(f"{identation}{file_name}")
            return True
        except IOError as e:
            print(f"{identation}Failed to create file: {file_name}. Error: {e}")
            return False
    else:
        print(f"{identation}{file_name} (file already exists)")
        return False


def _add_content_from_template(file, template_file: str, file_path: str, module_code_path: str, prefix: str):
    with open(os.path.join(TEMPLATE_DIRECTORY, template_file), 'r') as template:
        content = template.read()
        package_name = _path_to_package(os.path.dirname(file_path), module_code_path)
        content = _replace_case_insensitive(content, TEMPLATE_PREFIX, prefix)
        content = content.replace(PACKAGE_NAME_KEYWORD, package_name)
    file.write(content)

def _create_directory(path: str, depth: int = 0) -> bool:
    """Creates a directory at the specified path."""

    identation = _get_identation(depth)
    directory_name = path.split("/")[-1]
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"{identation}{directory_name}")
        return True
    else:
        print(f"{identation}{directory_name} (directory already exists)")
        return False


def _replace_case_insensitive(text: str, old: str, new: str) -> str:
    """Replace the text keeping the original case."""

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


def _get_identation(depth: int) -> str:
    identation = ""
    for i in range(depth):
        identation += "  "
    return identation