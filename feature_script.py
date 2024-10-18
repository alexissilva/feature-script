import os
import re

PREFIX_KEYWORD = "Prefix"

def create_file_or_directory(base_path: str, template_path: str, prefix: str, base_code_path: str, depth: int = 0):
    if not os.path.exists(template_path):
        print_indented(f"Template file does not exist: {template_path}.", depth)
        return     
    
    file_or_dir_name = os.path.basename(template_path)
    new_path = _get_path_with_prefix(base_path, file_or_dir_name, prefix)

    if os.path.isfile(template_path):
        create_file_from_template(new_path, template_path, prefix, base_code_path, depth)
    else:
        create_directory(new_path, depth)
        for sub_path in os.listdir(template_path):
            new_template = os.path.join(template_path, sub_path)
            create_file_or_directory(new_path, new_template, prefix, base_code_path, depth+1)
    


def _get_path_with_prefix(base_path: str, file_name: str, prefix: str) -> str:
    name_with_prefix = _replace_case_insensitive(file_name, PREFIX_KEYWORD, prefix)

    return os.path.join(base_path, name_with_prefix)

def create_file_from_template(file_path: str, template_path: str, prefix: str, base_code_path: str, depth: int = 0) -> bool:
    file_name = os.path.basename(file_path)
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                if template_path:
                    content = _get_content_from_template(file_path, template_path, prefix, base_code_path, depth)
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


def _get_content_from_template(file_path: str, template_file_path: str, prefix: str,  base_code_path: str, depth: int) -> str:
    try:
        with open(template_file_path, 'r') as template:
            content = template.read()
            content = _replace_case_insensitive(content, PREFIX_KEYWORD, prefix)
            package_pattern = r'^\s*package .*$'
            package_name = _path_to_package(file_path, base_code_path)
            content = re.sub(package_pattern, f"package {package_name}", content, flags=re.MULTILINE)
    except FileNotFoundError:
        print_indented(f"Template file not found: {template_file_path}.", depth)
        content = ""
    
    return content


def _replace_case_insensitive(text: str, old: str, new: str) -> str:
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


def _path_to_package(path: str, base_path: str) -> str:
    if os.path.isfile(path):
        path = os.path.dirname(path)
    relative_path = os.path.relpath(path, base_path)
    return relative_path.replace(os.sep, '.')


    
def create_directory(path: str, depth: int = 0) -> bool:
    directory_name = os.path.basename(path)
    if not os.path.exists(path):
        os.makedirs(path)
        print_indented(f"{directory_name}/", depth)
        return True
    else:
        print_indented(f"{directory_name}/ (it already existed)", depth)
        return False



def print_indented(message: str, depth: int = 0):
    identation = _get_indentation(depth)
    print(f"{identation}{message}")


def _get_indentation(depth: int) -> str:
    indentation = ""
    for _ in range(depth):
        indentation += "    "
    return indentation