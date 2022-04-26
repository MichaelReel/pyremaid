from os import path
from unittest.mock import call, MagicMock, mock_open, patch

from pyremaid.mermaid_tools import create_mermaid_flow_graph_from_links
from pyremaid.models import MermaidElement


def test_create_mermaid_flow_graph_from_links(
    no_mermaid_elements: list[MermaidElement],
    no_elements_graph: str,
) -> None:
    result = create_mermaid_flow_graph_from_links(no_mermaid_elements)
    assert result == no_elements_graph
