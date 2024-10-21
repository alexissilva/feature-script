import argparse
from instruction import read_instructions, process_instructions
from code_inserter import KotlinCodeInserter
from utils import read_lines, write_lines


def modify_file(file_path: str, instructions_file: str):
    instructions = read_instructions(instructions_file)
    original_lines = read_lines(file_path) 
    code_inserter = KotlinCodeInserter(original_lines)
    process_instructions(instructions, code_inserter)
    write_lines(file_path, code_inserter.lines)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Modify a specified file based on given instructions.')
    parser.add_argument('file', type=str, help='The name of the file to be modified.')
    parser.add_argument('instructions', type=str, help='The instructions for modifying the file.')

    args = parser.parse_args()
    modify_file(args.file, args.instructions)