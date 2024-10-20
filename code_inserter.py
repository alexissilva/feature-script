from abc import ABC, abstractmethod

class CodeInserter(ABC):
    @abstractmethod
    def insert_at_end_of_class(self, class_name: str, code: str):
        pass

    @abstractmethod
    def insert_at_end_of_function(self, function_name: str, code: str):
        pass

    @abstractmethod
    def insert_at_end_of_file(self, code: str):
        pass

    @abstractmethod
    def insert_import(self, code: str):
        pass


class KotlinCodeInserter(CodeInserter):
    def __init__(self, lines):
        self.lines = lines

    def insert_import(self, code: str):
        import_end = self.find_import_end()
        
        if import_end is not None:
            self.lines.insert(import_end + 1, f'{code}\n')
        else:
            self.insert_before_first_code_line(code)

    def insert_before_first_code_line(self, code: str):
        for index, line in enumerate(self.lines):
            if not line.startswith(('import', 'package')):
                self.lines.insert(index, f'{code}\n')
                return
        self.lines.append(f'\n{code}\n')

    def insert_at_end_of_class(self, class_name: str, code: str):
        class_end = self.find_class_end(class_name)
        if class_end is not None:
            self.lines.insert(class_end + 1, f'{code}\n')

    def insert_at_end_of_function(self, function_name: str, code: str):
        function_end = self.find_function_end(function_name)
        if function_end is not None:
            self.lines.insert(function_end + 1, f'{code}\n')

    def insert_at_end_of_file(self, code: str):
        self.lines.append(f'\n{code}\n')

    def find_import_end(self):
        for index, line in enumerate(self.lines):
            if not line.startswith(('import', 'package')):
                return index - 1
        return None

    def find_class_end(self, class_name: str):
        inside_class = False
        bracket_count = 0
        
        for index, line in enumerate(self.lines):
            if f'class {class_name}' in line:
                inside_class = True
            
            if inside_class:
                bracket_count += line.count('{')
                bracket_count -= line.count('}')
                if bracket_count == 0:
                    return index

        return None

    def find_function_end(self, function_name: str):
        inside_function = False
        bracket_count = 0
        
        for index, line in enumerate(self.lines):
            if f'fun {function_name}' in line:
                inside_function = True
            
            if inside_function:
                bracket_count += line.count('{')
                bracket_count -= line.count('}')
                if bracket_count == 0:
                    return index

        return None
