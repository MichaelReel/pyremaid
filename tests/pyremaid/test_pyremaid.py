from ast import AST
from unittest.mock import call, MagicMock, patch
from pyremaid.models import MermaidElement

from pyremaid.pyremaid import (
    create_mermaid_analysis_from_python,
    create_new_mermaid_analysis_for_file,
    get_global_input_table,
)


@patch("pyremaid.pyremaid.create_new_mermaid_analysis_for_file")
@patch("pyremaid.pyremaid.get_global_input_table")
@patch("pyremaid.pyremaid.find_all_python_files")
@patch("pyremaid.pyremaid.create_cleared_output_folder")
def test_create_mermaid_analysis_from_python(
    mock_create_cleared_output_folder: MagicMock,
    mock_find_all_python_files: MagicMock,
    mock_get_global_input_table: MagicMock,
    mock_create_new_mermaid_analysis_for_file: MagicMock,
    python_files: list[str],
    global_import_table: dict[str, str],
    input_path: str,
    output_path: str,
) -> None:

    mock_find_all_python_files.return_value = python_files
    mock_get_global_input_table.return_value = global_import_table

    create_mermaid_analysis_from_python(input_path=input_path, output_path=output_path)

    mock_create_cleared_output_folder.assert_called_once_with(output_path=output_path)
    mock_find_all_python_files.assert_called_once_with(input_path=input_path)
    mock_get_global_input_table.assert_called_once_with(
        input_path=input_path, python_files=python_files, output_root=output_path
    )
    assert mock_create_new_mermaid_analysis_for_file.call_count == len(python_files)
    mock_create_new_mermaid_analysis_for_file.assert_has_calls(
        calls=[
            call(
                input_path=input_path,
                output_path=output_path,
                global_import_table=global_import_table,
                in_file=in_file,
            )
            for in_file in python_files
        ]
    )


@patch("pyremaid.pyremaid.update_output_file")
@patch("pyremaid.pyremaid.create_markdown_content")
@patch("pyremaid.pyremaid.get_source_code_from_file")
@patch("pyremaid.pyremaid.get_output_file_path_for_input_file")
def test_create_new_mermaid_analysis_for_file_no_content(
    mock_get_output_file_path_for_input_file: MagicMock,
    mock_get_source_code_from_file: MagicMock,
    mock_create_markdown_content: MagicMock,
    mock_update_output_file: MagicMock,
    output_file: str,
    markdown_content: str,
    input_path: str,
    output_path: str,
    global_import_table: dict[str, str],
    input_file: str,
    relative_in_file: str,
) -> None:
    mock_get_output_file_path_for_input_file.return_value = output_file
    mock_get_source_code_from_file.return_value = None
    mock_create_markdown_content.return_value = markdown_content

    create_new_mermaid_analysis_for_file(
        input_path=input_path,
        output_path=output_path,
        global_import_table=global_import_table,
        in_file=input_file,
    )

    mock_get_output_file_path_for_input_file.assert_called_once_with(
        input_path=relative_in_file, output_root=output_path
    )
    mock_get_source_code_from_file.assert_called_once_with(input_file=input_file)
    mock_create_markdown_content.assert_called_once_with(
        input_file=input_file,
        import_list=[],
        global_import_table=global_import_table,
        mermaid_diagrams=[],
        debug_dump="",
    )
    mock_update_output_file.assert_called_once_with(
        content=markdown_content, output_file=output_file
    )


@patch("pyremaid.pyremaid.update_output_file")
@patch("pyremaid.pyremaid.create_markdown_content")
@patch("pyremaid.pyremaid.get_ast_root_node_for_file")
@patch("pyremaid.pyremaid.get_source_code_from_file")
@patch("pyremaid.pyremaid.get_output_file_path_for_input_file")
def test_create_new_mermaid_analysis_for_file_no_ast(
    mock_get_output_file_path_for_input_file: MagicMock,
    mock_get_source_code_from_file: MagicMock,
    mock_get_ast_root_node_for_file: MagicMock,
    mock_create_markdown_content: MagicMock,
    mock_update_output_file: MagicMock,
    output_file: str,
    file_content: str,
    markdown_content: str,
    input_path: str,
    output_path: str,
    global_import_table: dict[str, str],
    input_file: str,
    relative_in_file: str,
) -> None:
    mock_get_output_file_path_for_input_file.return_value = output_file
    mock_get_source_code_from_file.return_value = file_content
    mock_get_ast_root_node_for_file.return_value = None
    mock_create_markdown_content.return_value = markdown_content

    create_new_mermaid_analysis_for_file(
        input_path=input_path,
        output_path=output_path,
        global_import_table=global_import_table,
        in_file=input_file,
    )

    mock_get_output_file_path_for_input_file.assert_called_once_with(
        input_path=relative_in_file, output_root=output_path
    )
    mock_get_source_code_from_file.assert_called_once_with(input_file=input_file)
    mock_get_ast_root_node_for_file.assert_called_once_with(
        source_code=file_content, input_file=input_file
    )
    mock_create_markdown_content.assert_called_once_with(
        input_file=input_file,
        import_list=[],
        global_import_table=global_import_table,
        mermaid_diagrams=[],
        debug_dump="",
    )
    mock_update_output_file.assert_called_once_with(
        content=markdown_content, output_file=output_file
    )


# TODO: The size of the mock list here suggests the target code could be refactored
@patch("pyremaid.pyremaid.update_output_file")
@patch("pyremaid.pyremaid.create_markdown_content")
@patch("pyremaid.pyremaid.create_mermaid_flow_graph_from_links")
@patch("pyremaid.pyremaid.create_mermaid_model_from_ast_model")
@patch("pyremaid.pyremaid.get_used_import_list")
@patch("pyremaid.pyremaid.get_markdown_dump_for_ast_node")
@patch("pyremaid.pyremaid.get_ast_root_node_for_file")
@patch("pyremaid.pyremaid.get_source_code_from_file")
@patch("pyremaid.pyremaid.get_output_file_path_for_input_file")
def test_create_new_mermaid_analysis_for_file(
    mock_get_output_file_path_for_input_file: MagicMock,
    mock_get_source_code_from_file: MagicMock,
    mock_get_ast_root_node_for_file: MagicMock,
    mock_get_markdown_dump_for_ast_node,
    mock_get_used_import_list,
    mock_create_mermaid_model_from_ast_model,
    mock_create_mermaid_flow_graph_from_links,
    mock_create_markdown_content: MagicMock,
    mock_update_output_file: MagicMock,
    output_file: str,
    file_content: str,
    ast: AST,
    debug_dump: str,
    import_list: list[str],
    mermaid_element_list: list[MermaidElement],
    mermaid_diagram: str,
    markdown_content: str,
    input_path: str,
    output_path: str,
    global_import_table: dict[str, str],
    mermaid_diagrams: list[str],
    input_file: str,
    relative_in_file: str,
) -> None:
    mock_get_output_file_path_for_input_file.return_value = output_file
    mock_get_source_code_from_file.return_value = file_content
    mock_get_ast_root_node_for_file.return_value = ast
    mock_get_markdown_dump_for_ast_node.return_value = debug_dump
    mock_get_used_import_list.return_value = import_list
    mock_create_mermaid_model_from_ast_model.return_value = mermaid_element_list
    mock_create_mermaid_flow_graph_from_links.return_value = mermaid_diagram
    mock_create_markdown_content.return_value = markdown_content

    create_new_mermaid_analysis_for_file(
        input_path=input_path,
        output_path=output_path,
        global_import_table=global_import_table,
        in_file=input_file,
    )

    mock_get_output_file_path_for_input_file.assert_called_once_with(
        input_path=relative_in_file, output_root=output_path
    )
    mock_get_source_code_from_file.assert_called_once_with(input_file=input_file)
    mock_get_ast_root_node_for_file.assert_called_once_with(
        source_code=file_content, input_file=input_file
    )
    mock_get_markdown_dump_for_ast_node.assert_called_once_with(ast_node=ast)
    mock_get_used_import_list.assert_called_once_with(ast_node=ast)
    mock_create_mermaid_model_from_ast_model.assert_called_once_with(model=ast)
    mock_create_mermaid_flow_graph_from_links.assert_called_once_with(
        elements=mermaid_element_list
    )
    mock_create_markdown_content.assert_called_once_with(
        input_file=input_file,
        import_list=import_list,
        global_import_table=global_import_table,
        mermaid_diagrams=mermaid_diagrams,
        debug_dump=debug_dump,
    )
    mock_update_output_file.assert_called_once_with(
        content=markdown_content, output_file=output_file
    )


@patch("pyremaid.pyremaid.get_all_imports_from_files")
def test_get_global_input_table_no_imports(
    mock_get_all_imports_from_files: MagicMock,
    no_imports_from_files: dict[str, str],
    input_path: str,
    python_files: list[str],
    output_path: str,
) -> None:
    mock_get_all_imports_from_files.return_value = no_imports_from_files

    result = get_global_input_table(
        input_path=input_path, python_files=python_files, output_root=output_path
    )

    mock_get_all_imports_from_files.assert_called_once_with(
        input_path=input_path, python_files=python_files
    )
    assert result == {}


@patch("pyremaid.pyremaid.get_all_imports_from_files")
def test_get_global_input_table(
    mock_get_all_imports_from_files: MagicMock,
    all_imports_from_files: dict[str, str],
    input_path: str,
    python_files: list[str],
    output_path: str,
) -> None:
    mock_get_all_imports_from_files.return_value = all_imports_from_files

    result = get_global_input_table(
        input_path=input_path, python_files=python_files, output_root=output_path
    )

    mock_get_all_imports_from_files.assert_called_once_with(
        input_path=input_path, python_files=python_files
    )
    assert result == {
        "parent dir": "output path/parent dir.md",
        "python file 1": "output path/python file 1.md",
        "python file 2": "",
    }
