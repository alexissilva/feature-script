# Defining the FSNode class to represent files and directories
class FSNode:
    def __init__(self, name: str, is_file: bool = False, template_file: str = None, sub_nodes=None):
        if sub_nodes is None:
            sub_nodes = []
        self.name = name
        self.is_file = is_file
        self.template_file = template_file
        self.sub_nodes = sub_nodes