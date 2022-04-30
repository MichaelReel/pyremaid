from pyremaid.mermaid_tools import create_mermaid_flow_graph_from_links
from pyremaid.models import (
    MermaidBlock,
    MermaidClass,
    MermaidElement,
    MermaidFor,
    MermaidFunction,
    MermaidLink,
    MermaidModule,
    MermaidNode,
)


def test_create_blank_mermaid_flow_graph(
    no_mermaid_elements: list[MermaidElement],
    no_elements_graph: str,
) -> None:
    result = create_mermaid_flow_graph_from_links(no_mermaid_elements)
    assert result == no_elements_graph


def test_create_graph_from_node(mermaid_node: MermaidNode, node_graph: str) -> None:
    result = create_mermaid_flow_graph_from_links([mermaid_node])
    assert result == node_graph


def test_create_graph_from_link(mermaid_link: MermaidLink, link_graph: str) -> None:
    result = create_mermaid_flow_graph_from_links([mermaid_link])
    assert result == link_graph


def test_create_graph_from_block(mermaid_block: MermaidBlock, block_graph: str) -> None:
    result = create_mermaid_flow_graph_from_links([mermaid_block])
    assert result == block_graph


def test_create_graph_from_module(
    mermaid_module: MermaidModule, module_graph: str
) -> None:
    result = create_mermaid_flow_graph_from_links([mermaid_module])
    assert result == module_graph


def test_create_graph_from_function(
    mermaid_function: MermaidFunction, function_graph: str
) -> None:
    result = create_mermaid_flow_graph_from_links([mermaid_function])
    assert result == function_graph


def test_create_graph_from_class(mermaid_class: MermaidClass, class_graph: str) -> None:
    result = create_mermaid_flow_graph_from_links([mermaid_class])
    assert result == class_graph


def test_create_graph_from_for(mermaid_for: MermaidFor, for_graph: str) -> None:
    result = create_mermaid_flow_graph_from_links([mermaid_for])
    assert result == for_graph


def test_create_mermaid_flow_graph_from_structure(
    mermaid_elements: list[MermaidElement],
    elements_graph: str,
) -> None:
    result = create_mermaid_flow_graph_from_links(mermaid_elements)
    assert result == elements_graph
