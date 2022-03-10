from ast import AST
from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class MermaidElement:
    pass


@dataclass(unsafe_hash=True, frozen=True)
class MermaidNode(MermaidElement):
    ast_node: AST
    mermaid_safe_name: str
    display_name: str


@dataclass(frozen=True)
class MermaidLink(MermaidElement):
    from_: MermaidNode
    to: MermaidNode


@dataclass(unsafe_hash=True, frozen=True)
class MermaidBlock(MermaidNode):
    block_contents: list[MermaidLink] = field(default_factory=list)


@dataclass(unsafe_hash=True, frozen=True)
class MermaidModule(MermaidBlock):
    pass


@dataclass(unsafe_hash=True, frozen=True)
class MermaidFunction(MermaidBlock):
    pass
