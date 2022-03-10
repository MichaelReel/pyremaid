from ast import AST
from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class MermaidNode:
    ast_node: AST
    mermaid_safe_name: str


@dataclass
class MermaidLink:
    from_: MermaidNode
    to: MermaidNode
