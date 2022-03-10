from ast import AST, Import, ImportFrom, NodeVisitor
from models import MermaidLink, MermaidNode
from typing import Any, Optional


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


class LinkGenerator(NodeVisitor):
    def __init__(self) -> None:
        self.links : list[MermaidLink] = []
        self.prev_node : Optional[AST] = None
        self.count : int = 0

    def visit_Import(self, node: Import) -> None:
        pass

    def visit_ImportFrom(self, node: ImportFrom) -> None:
        pass

    def generic_visit(self, node: AST) -> Any:
        mermaid_data = MermaidNode(
            ast_node=node,
            mermaid_safe_name=f"node_{self.count}"
        )
        self.count += 1
        if self.prev_node:
            self.links.append(MermaidLink(from_=self.prev_node, to=mermaid_data))
        self.prev_node = mermaid_data

        # Don't forget to visit the children nodes
        return super().generic_visit(node)

    def get_list_of_links(self) -> list[MermaidLink]:
        return self.links
