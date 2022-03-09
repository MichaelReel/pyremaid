from ast import AST, Import, ImportFrom, NodeVisitor
from typing import Any


class ImportNodeFinder(NodeVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.found_imports = []

    def visit_Import(self, node: Import) -> Any:
        self.found_imports.append(node)
        return super().visit_Import(node)

    def visit_ImportFrom(self, node: ImportFrom) -> Any:
        self.found_imports.append(node)
        return super().visit_ImportFrom(node)

    def get_found_imports(self) -> list[AST]:
        return self.found_imports
