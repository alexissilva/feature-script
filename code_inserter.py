import re
from abc import ABC, abstractmethod

class CodeInserter(ABC):
    @abstractmethod
    def insert_at_end_of_class(self, class_name: str, code: str) -> bool:
        pass

    @abstractmethod
    def insert_at_end_of_function(self, function_name: str, code: str) -> bool:
        pass

    @abstractmethod
    def insert_at_end_of_block(self, block_name: str, code: str) -> bool:
        pass

    @abstractmethod
    def insert_at_end_of_file(self, code: str) -> bool:
        pass

    @abstractmethod
    def insert_import(self, code: str) -> bool:
        pass

INDENTATION_LEVEL = '    '
class KotlinCodeInserter(CodeInserter):

    def __init__(self, original_lines: str):
        self.lines = original_lines.copy()

    def insert_import(self, code: str) -> bool:
        import_line = f'{code}\n'
        import_index = self.find_import_index()
        package_index = self.find_package_index()

        if import_index is not None:
            self.insert_line_by_line(import_index + 1, import_line)
            return True
        elif package_index is not None:
            self.insert_line_by_line(package_index + 1, f"\n{import_line}")
            return True
        else:
            self.insert_line_by_line(0, import_line)
            return True

    def insert_at_end_of_class(self, class_name: str, code: str) -> bool:
        return self.insert_at_end_of_bracket_element(f"class {class_name}", code)

    def insert_at_end_of_function(self, function_name: str, code: str) -> bool:
        return self.insert_at_end_of_bracket_element(f"fun {function_name}", code)

    
    def insert_at_end_of_block(self, block_name: str, code: str) -> bool:
        return self.insert_at_end_of_bracket_element(block_name, code)


    def insert_at_end_of_file(self, code: str) -> bool:
        self.insert_line_by_line(len(self.lines), code)
        return True


    def find_import_index(self):
        last_import_index = None
        for index, line in enumerate(self.lines):
            if line.startswith('import'):
                last_import_index = index
        return last_import_index

    def find_package_index(self):
        for index, line in enumerate(self.lines):
            if line.startswith('package'):
                return index
        return None


    def insert_at_end_of_bracket_element(self, element_pattern: str, code: str) -> bool:
        element_end = self.find_bracket_element_end(element_pattern)
        if element_end is not None:
            indentation = self.get_previous_indentation(element_end)
            self.insert_line_by_line(element_end, code, indentation)
            return True
        return False

    def find_bracket_element_end(self, element_pattern: str):
        inside_element = False
        inside_brackets = False
        bracket_count = 0
        current_block = ""
        
        for index, line in enumerate(self.lines):
            current_block += line + "\n"

            if not inside_element and re.search(element_pattern, current_block):
                inside_element = True
            
            if inside_element:
                bracket_count += line.count('{')
                if bracket_count > 0:
                    inside_brackets = True
                bracket_count -= line.count('}')
                if inside_brackets and bracket_count == 0:
                    return index

        return None

    def get_previous_indentation(self, current_line_index: int) -> str:
        for i in range(current_line_index-1, -1, -1):
            line = self.lines[i]
            if line.strip():
                indentation = line[:len(line) - len(line.lstrip())]
                if line.strip().endswith('{'):
                    indentation += INDENTATION_LEVEL
                return indentation
        
        return ''
    

    def insert_line_by_line(self, start_index: str, code: str, indentation: str = ''):
        for index, line in enumerate(code.splitlines()):
            self.lines.insert(start_index+index, f"{indentation}{line}\n")

    

