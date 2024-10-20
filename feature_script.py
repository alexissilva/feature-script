import os
import re
from typing import List
from utils import is_subpath, print_indented, replace_keywords, get_test_path_from_source_path
from config import IGNORE_FILES
from keyword_script import KeywordScript


def create_component(destination: str, template_path: str, keywords: list, root_path: str, name: str, component_type: str, test_template_path: str = None):
    print(f"Creating {component_type} '{name}'...")
    print("Creating directories and files:")
    try:
        create_file_or_directory(destination, template_path, keywords, root_path)
        print(f"{component_type.capitalize()} '{name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating {component_type.lower()}: {e}")


    if test_template_path:
        test_destination = get_test_path_from_source_path(destination)
        test_root = get_test_path_from_source_path(root_path)
        print()
        create_component(test_destination, test_template_path, keywords, test_root, name, f"test of {component_type}")


def create_file_or_directory(base_path: str, template_path: str, keywords: List[KeywordScript], root_code_path: str, depth: int = 0):
    if not os.path.exists(template_path):
        print_indented(f"Template file does not exist: {template_path}.", depth)
        return     
    
    file_or_dir_name = os.path.basename(template_path)
    if file_or_dir_name in IGNORE_FILES:
        return

    new_path = _get_path_with_keywords(base_path, file_or_dir_name, keywords)

    if os.path.isfile(template_path):
        _create_file_from_template(new_path, template_path, keywords, root_code_path, depth)
    else:
        _create_directory(new_path, depth)
        for sub_path in os.listdir(template_path):
            new_template = os.path.join(template_path, sub_path)
            create_file_or_directory(new_path, new_template, keywords, root_code_path, depth+1)
    


def _get_path_with_keywords(base_path: str, file_name: str, keywords: List[KeywordScript]) -> str:
    name_with_keywords = replace_keywords(file_name, keywords)
    return os.path.join(base_path, name_with_keywords)

def _create_file_from_template(file_path: str, template_path: str, keywords: List[KeywordScript], root_code_path: str, depth: int = 0) -> bool:
    file_name = os.path.basename(file_path)
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                if template_path:
                    content = _get_content_from_template(file_path, template_path, keywords, root_code_path, depth)
                    file.write(content)
                else:
                    file.write("")
            print_indented(f"{file_name}", depth)
            return True
        except IOError as e:
            print_indented(f"Failed to create file: {file_path}. Error: {e}", depth)
            return False
    else:
        print_indented(f"{file_name} (it already existed)", depth)
        return False


def _get_content_from_template(file_path: str, template_file_path: str, keywords: List[KeywordScript],  root_code_path: str, depth: int) -> str:
    try:
        with open(template_file_path, 'r') as template:
            content = template.read()
            content = replace_keywords(content, keywords)
            content = _replace_package(content, file_path, root_code_path)
    except FileNotFoundError:
        print_indented(f"Template file not found: {template_file_path}.", depth)
        content = ""
    
    return content


def _replace_package(text: str, file_path: str, root_code_path: str) -> str:
        package_pattern = r'^\s*package .*$'
        package_name = _path_to_package(file_path, root_code_path)
        return re.sub(package_pattern, f"package {package_name}", text, flags=re.MULTILINE)


def _path_to_package(path: str, base_path: str) -> str:
    if not is_subpath(base_path, path):
        return ""

    if os.path.isfile(path):
        path = os.path.dirname(path)
    relative_path = os.path.relpath(path, base_path)
    return relative_path.replace(os.sep, '.')


    
def _create_directory(path: str, depth: int = 0) -> bool:
    directory_name = os.path.basename(path)
    if not os.path.exists(path):
        os.makedirs(path)
        print_indented(f"{directory_name}/", depth)
        return True
    else:
        print_indented(f"{directory_name}/ (it already existed)", depth)
        return False

