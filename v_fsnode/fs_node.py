class FSNode:
    """Represents a file or directory in a hierarchical structure."""

    def __init__(self, name, is_file=False, template_file=None, sub_nodes=[], optional=False):
        self.name = name
        self.is_file = is_file
        self.template_file = template_file
        self.sub_nodes = sub_nodes
        self.optional = optional