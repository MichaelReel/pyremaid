from ast import AST
from pytest import mark
from unittest.mock import MagicMock, patch

from pyremaid.ast_tools.ast_tools import (
    get_ast_root_node_for_file,
    get_markdown_dump_for_ast_node,
    get_used_import_list,
    create_mermaid_model_from_ast_model,
)
from pyremaid.models import MermaidElement


@mark.parametrize("source_code", ["dummy source code"])
@patch("pyremaid.ast_tools.ast_tools.parse")
def test_get_ast_root_node_for_file(
    mock_parse: MagicMock, source_code: str, input_file: str, ast: AST
) -> None:
    mock_parse.return_value = ast

    result = get_ast_root_node_for_file(source_code=source_code, input_file=input_file)

    assert result == ast
    mock_parse.assert_called_once_with(
        source=source_code, filename=input_file, mode="exec", type_comments=True
    )


@mark.parametrize("dump_code", ["dummy dump code"])
@patch("pyremaid.ast_tools.ast_tools.dump")
def test_get_markdown_dump_for_ast_node(
    mock_dump: MagicMock, ast: AST, dump_code: str
) -> None:
    mock_dump.return_value = dump_code

    result = get_markdown_dump_for_ast_node(ast_node=ast)

    assert result == dump_code
    mock_dump.assert_called_once_with(
        node=ast, annotate_fields=True, include_attributes=True, indent=2
    )


@patch("pyremaid.ast_tools.ast_tools.ImportNodeFinder")
def test_get_used_import_list(
    MockImportNodeFinder: MagicMock, ast: AST, import_list: list[str]
) -> None:
    mock_finder = MockImportNodeFinder.return_value
    mock_finder.get_found_imports.return_value = import_list

    result = get_used_import_list(ast_node=ast)

    assert result == import_list
    mock_finder.visit.assert_called_once_with(node=ast)
    mock_finder.get_found_imports.assert_called_once()


@patch("pyremaid.ast_tools.ast_tools.BlockGenerator")
def test_create_mermaid_model_from_ast_model(
    MockBlockGenerator: MagicMock, ast: AST, mermaid_element_list: list[MermaidElement]
) -> None:
    mock_generator = MockBlockGenerator.return_value
    mock_generator.get_list_of_elements.return_value = mermaid_element_list

    result = create_mermaid_model_from_ast_model(model=ast)

    assert result == mermaid_element_list
    mock_generator.visit.assert_called_once_with(node=ast)
    mock_generator.get_list_of_elements.assert_called_once()
