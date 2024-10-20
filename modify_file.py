from instructions import read_instructions, process_instructions
from code_inserter import KotlinCodeInserter

def modify_file(file_path: str, instruction_file: str):
    instructions = read_instructions(instruction_file)
    lines = read_lines(file_path) 
    code_inserter = KotlinCodeInserter(lines)
    process_instructions(instructions, code_inserter)
    write_lines(file_path, code_inserter.lines)


def read_lines(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return file.readlines()

def write_lines(file_path: str, lines: list):
    with open(file_path, 'w') as file:
        file.writelines(lines)