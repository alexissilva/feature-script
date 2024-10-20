from abc import ABC, abstractmethod

class CodeInserter(ABC):
    @abstractmethod
    def insert_at_end_of_class(self, class_name: str, code: str) -> bool:
        pass

    @abstractmethod
    def insert_at_end_of_function(self, function_name: str, code: str) -> bool:
        pass

    @abstractmethod
    def insert_at_end_of_file(self, code: str) -> bool:
        pass

    @abstractmethod
    def insert_import(self, code: str) -> bool:
        pass

class KotlinCodeInserter(CodeInserter):
    def __init__(self, lines: list):
        self.lines = lines

    def insert_import(self, code: str) -> bool:
        import_line = f'{code}\n'
        import_index = self.find_import_index()
        package_index = self.find_package_index()

        if import_index is not None:
            self.lines.insert(import_index + 1, import_line)
            return True
        elif package_index is not None:
            self.lines.insert(package_index + 1, import_line)
            return True
        else:
            self.lines.insert(0, import_line)
            return True

    def insert_at_end_of_class(self, class_name: str, code: str) -> bool:
        class_end = self.find_class_end(class_name)
        if class_end is not None:
            self.lines.insert(class_end + 1, f'{code}\n')
            return True
        return False

    def insert_at_end_of_function(self, function_name: str, code: str) -> bool:
        function_end = self.find_function_end(function_name)
        if function_end is not None:
            self.lines.insert(function_end + 1, f'{code}\n')
            return True
        return False

    def insert_at_end_of_file(self, code: str) -> bool:
        self.lines.append(f'\n{code}\n')
        return True

    def find_import_index(self):
        last_import_index = None
        for index, line in enumerate(self.lines):
            if line.strip() == '':
                continue
            if line.startswith('import'):
                last_import_index = index
        return last_import_index

    def find_package_index(self):
        for index, line in enumerate(self.lines):
            if line.strip() == '':
                continue
            if line.startswith('package'):
                return index
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