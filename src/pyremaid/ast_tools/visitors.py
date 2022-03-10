from ast import AST, Import, ImportFrom, Module, NodeVisitor
from models import MermaidBlock, MermaidElement, MermaidLink, MermaidNode
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
        self.elements : list[MermaidElement] = []
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
            self.elements.append(MermaidLink(from_=self.prev_node, to=mermaid_data))
        self.prev_node = mermaid_data

        # Don't forget to visit the children nodes
        return super().generic_visit(node)

    def get_list_of_elements(self) -> list[MermaidLink]:
        return self.elements


class BlockGenerator(NodeVisitor):
    def __init__(self) -> None:
        self.elements : list[MermaidElement] = []
        self.count : int = 0

    def _count(self) -> int:
        value = self.count
        self.count +=1
        return value

    def visit_Module(self, block_node: Module) -> Any:
        """This is a block, we might want a subgraph, so parse content"""
        link_generator = LinkGenerator()
        link_generator.visit(node=block_node)

        mermaid_block = MermaidBlock(
            ast_node = block_node,
            mermaid_safe_name = f"module_{self._count()}",
            block_contents = link_generator.get_list_of_elements()
        )

        self.elements.append(mermaid_block)

    def generic_visit(self, _node: AST) -> Any:
        """Non block nodes are not interesting here"""
        pass

    def get_list_of_elements(self) -> list[MermaidElement]:
        return self.elements
