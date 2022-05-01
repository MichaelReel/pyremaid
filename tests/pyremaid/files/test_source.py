from unittest.mock import MagicMock, mock_open, patch
from pytest import mark

from pyremaid.files.source import (
    find_all_python_files,
    get_source_code_from_file,
    get_import_name_from_path,
)
from tests.conftest import file_content_data


@patch("pyremaid.files.source.walk")
def test_find_all_python_files(
    mock_walk: MagicMock,
    input_path: str,
    walked_files: list[tuple[str, list[str], list[str]]],
    resolved_python_files: list[str],
) -> None:
    mock_walk.return_value = walked_files

    found_python_files = find_all_python_files(input_path=input_path)

    assert found_python_files == resolved_python_files


@patch("pyremaid.files.source.open", mock_open(read_data=file_content_data))
def test_get_source_code_from_file(
    input_file: str,
    file_content: str,
) -> None:

    test_file_content = get_source_code_from_file(input_file=input_file)

    assert test_file_content == file_content


@mark.parametrize(
    "input_path,input_file,expected_result",
    [
        ("", "", ""),
        (
            "test_input_path",
            "test_input_path/other_path/python_file.py",
            ".other_path.python_file",
        ),
        (
            "",
            "__init__.py",
            ".",
        ),
        (
            "b",
            "b/__init__.py",
            "",
        ),
        (
            "c",
            "c/d/__init__.py",
            ".d",
        ),
    ],
)
def test_get_import_name_from_path(
    input_path: str, input_file: str, expected_result: str
) -> None:

    test_import_name = get_import_name_from_path(
        input_path=input_path, input_file=input_file
    )

    assert test_import_name == expected_result
