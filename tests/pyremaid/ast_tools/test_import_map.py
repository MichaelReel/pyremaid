from ast import AST
from unittest.mock import MagicMock, call, patch
from pyremaid.ast_tools.import_map import get_all_imports_from_files


def test_get_no_imports_from_no_files(
    input_path: str, no_python_files: list[str], empty_imports_table: dict[str, str]
) -> None:
    result = get_all_imports_from_files(input_path, no_python_files)

    assert result == empty_imports_table


@patch("pyremaid.ast_tools.import_map.get_used_import_list")
@patch("pyremaid.ast_tools.import_map.get_ast_root_node_for_file")
@patch("pyremaid.ast_tools.import_map.get_source_code_from_file")
@patch("pyremaid.ast_tools.import_map.get_import_name_from_path")
def test_get_all_imports_from_files(
    mock_get_import_name_from_path: MagicMock,
    mock_get_source_code_from_file: MagicMock,
    mock_get_ast_root_node_for_file: MagicMock,
    mock_get_used_import_list: MagicMock,
    import_list: list[str],
    file_content: str,
    ast: AST,
    input_path: str,
    python_files: list[str],
    all_imports_table: dict[str, str],
) -> None:
    mock_get_import_name_from_path.side_effect = import_list
    mock_get_source_code_from_file.side_effect = [file_content, file_content, None]
    mock_get_ast_root_node_for_file.side_effect = [ast, None, None]
    mock_get_used_import_list.return_value = import_list

    result = get_all_imports_from_files(input_path, python_files)

    mock_get_import_name_from_path.assert_has_calls(
        calls=[call(input_path=input_path, input_file=file) for file in python_files]
    )
    mock_get_source_code_from_file.assert_has_calls(
        calls=[call(input_file=in_file) for in_file in python_files]
    )
    mock_get_ast_root_node_for_file.assert_has_calls(
        calls=[
            call(source_code=file_content, input_file=python_files[0]),
            call(source_code=file_content, input_file=python_files[1]),
        ]
    )
    mock_get_used_import_list.assert_called_with(ast_node=ast)
    assert result == all_imports_table
