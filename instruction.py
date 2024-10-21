from code_inserter import CodeInserter

INSERT_TAG = '//insert:'
TARGET_TAG = '//target:'
END_OF_FILE_ACTION = 'end of file'
END_OF_FUNCTION_ACTION = 'end of function'
IMPORT_ACTION = 'import'
END_OF_CLASS_ACTION = 'end of class'
END_OF_BLOCK_ACTION = "end of block"


class Instruction:
    def __init__(self, action, target, code):
        self.action = action
        self.target = target
        self.code = code


def read_instructions(file_path: str) -> list:
    instructions = []
    current_code = ""
    current_action = None
    current_target = None

    with open(file_path, 'r') as file:
        for line in file:
            if line.lower().startswith(INSERT_TAG):
                if current_action is not None:
                    instructions.append(Instruction(current_action, current_target, current_code))
                current_action = line.split(INSERT_TAG)[1].strip()
                current_target = None
                current_code = ""
            elif line.lower().startswith(TARGET_TAG):
                current_target = line.split(TARGET_TAG)[1].strip()
            else:
                current_code += line

        if current_action is not None:
            instructions.append(Instruction(current_action, current_target, current_code))

    return instructions


def process_instructions(instructions: list, inserter: CodeInserter):
    for instr in instructions:
        code = instr.code.strip()
        if instr.action.lower() == END_OF_FILE_ACTION.lower():
            inserter.insert_at_end_of_file(code)
        elif instr.action.lower() == END_OF_FUNCTION_ACTION.lower():
            if instr.target:
                inserter.insert_at_end_of_function(instr.target, code)
        elif instr.action.lower() == IMPORT_ACTION.lower():
            inserter.insert_import(code)
        elif instr.action.lower() == END_OF_CLASS_ACTION.lower():
            if instr.target:
                inserter.insert_at_end_of_class(instr.target, code)
        elif instr.action.lower() == END_OF_BLOCK_ACTION.lower():
            if instr.target:
                inserter.insert_at_end_of_block(instr.target, code)