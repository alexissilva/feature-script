import os
import re
from typing import List
from utils import is_subpath, print_indented, replace_keywords, get_test_path_from_source_path
from config import IGNORE_FILES
from keyword_script import KeywordScript


def create_component(destination: str, template_path: str, keywords: list, base_package: str, name: str, component_type: str, test_template_path: str = None):
    print(f"Creating {component_type} '{name}'...")
    print("Creating directories and files:")
    try:
        create_file_or_directory(destination, template_path, keywords, base_package)
        print(f"{component_type.capitalize()} '{name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating {component_type.lower()}: {e}")


    if test_template_path:
        print()
        test_destination = get_test_path_from_source_path(destination)
        test_root = get_test_path_from_source_path(base_package)
        create_component(test_destination, test_template_path, keywords, test_root, name, f"test of {component_type}")


def create_file_or_directory(base_path: str, template_path: str, keywords: List[KeywordScript], base_package: str, depth: int = 0):
    if not os.path.exists(template_path):
        print_indented(f"Template file does not exist: {template_path}.", depth)
        return     
    
    file_or_dir_name = os.path.basename(template_path)
    if file_or_dir_name in IGNORE_FILES:
        return

    new_path = _get_path_with_keywords(base_path, file_or_dir_name, keywords)

    if os.path.isfile(template_path):
        _create_file_from_template(new_path, template_path, keywords, base_package, depth)
    else:
        _create_directory(new_path, depth)
        for sub_path in os.listdir(template_path):
            new_template = os.path.join(template_path, sub_path)
            new_package = f"{base_package}.{file_or_dir_name}"
            create_file_or_directory(new_path, new_template, keywords, new_package, depth+1)


def _get_path_with_keywords(base_path: str, file_name: str, keywords: List[KeywordScript]) -> str:
    name_with_keywords = replace_keywords(file_name, keywords)
    return os.path.join(base_path, name_with_keywords)

def _create_file_from_template(file_path: str, template_path: str, keywords: List[KeywordScript], package: str, depth: int = 0) -> bool:
    file_name = os.path.basename(file_path)
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                if template_path:
                    content = _get_content_from_template(template_path, keywords, package, depth)
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


def _get_content_from_template(template_file_path: str, keywords: List[KeywordScript], package: str, depth: int) -> str:
    try:
        with open(template_file_path, 'r') as template:
            content = template.read()
            content = _replace_package(content, package)
            content = replace_keywords(content, keywords)
    except FileNotFoundError:
        print_indented(f"Template file not found: {template_file_path}.", depth)
        content = ""
    
    return content


def _replace_package(text: str, package_name: str) -> str:
        package_pattern = r'^\s*package .*$'
        return re.sub(package_pattern, f"package {package_name}", text, flags=re.MULTILINE)


    
def _create_directory(path: str, depth: int = 0) -> bool:
    directory_name = os.path.basename(path)
    if not os.path.exists(path):
        os.makedirs(path)
        print_indented(f"{directory_name}/", depth)
        return True
    else:
        print_indented(f"{directory_name}/ (it already existed)", depth)
        return False

