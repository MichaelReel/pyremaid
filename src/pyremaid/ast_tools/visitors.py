from ast import Import, ImportFrom, NodeVisitor


class ImportNodeFinder(NodeVisitor):
    def __init__(self) -> None:
        self.found_imports : list[str] = []

    def visit_Import(self, node: Import) -> None:
        for i in node.names:
            self.found_imports.append(f"{i.name}.*")

    def visit_ImportFrom(self, node: ImportFrom) -> None:
        module = node.module
        for i in node.names:
            self.found_imports.append(f"{module}.{i.name}")

    def get_found_imports(self) -> list[str]:
        return self.found_imports
