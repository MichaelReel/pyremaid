from pytest import fixture
from unittest.mock import call, MagicMock, patch


from pyremaid.pyremaid import create_mermaid_analysis_from_python


@fixture
def input_path() -> str:
    return "input path"


@fixture
def output_path() -> str:
    return "output path"


@fixture
def python_files() -> list[str]:
    return ["python file 1", "python file 2"]


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
