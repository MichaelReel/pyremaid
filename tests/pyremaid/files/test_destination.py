from os import path
from unittest.mock import call, MagicMock, mock_open, patch

from pyremaid.files.destination import (
    _create_output_folder,
    create_cleared_output_folder,
    get_output_file_path_for_input_file,
    update_output_file,
)


@patch("pyremaid.files.destination.path.isdir")
@patch("pyremaid.files.destination.makedirs")
def test_create_output_folder(
    mock_makedirs: MagicMock,
    mock_path_isdir: MagicMock,
    output_path: str,
) -> None:
    mock_path_isdir.return_value = False

    _create_output_folder(output_path=output_path)

    mock_makedirs.assert_called_with(output_path)


@patch("pyremaid.files.destination.path.isdir")
@patch("pyremaid.files.destination.makedirs")
def test_create_output_folder_already_exists(
    mock_makedirs: MagicMock,
    mock_path_isdir: MagicMock,
    output_path: str,
) -> None:
    mock_path_isdir.return_value = True

    _create_output_folder(output_path=output_path)

    mock_makedirs.assert_not_called()


@patch("pyremaid.files.destination.rmdir")
@patch("pyremaid.files.destination.remove")
@patch("pyremaid.files.destination.walk")
@patch("pyremaid.files.destination._create_output_folder")
def test_create_cleared_output_folder(
    mock_create_output_folder: MagicMock,
    mock_walk: MagicMock,
    mock_remove: MagicMock,
    mock_rmdir: MagicMock,
    output_path: str,
    root_path: str,
    walked_files: list[tuple[str, list[str], list[str]]],
    walked_directory_names: list[str],
    walked_file_names: list[str],
) -> None:
    mock_walk.return_value = walked_files

    create_cleared_output_folder(output_path=output_path)

    mock_create_output_folder.assert_called_with(output_path=output_path)
    mock_walk.assert_called_with(output_path, topdown=False)
    mock_remove.assert_has_calls(
        calls=[call(path.join(root_path, file_name)) for file_name in walked_file_names]
    )
    mock_rmdir.assert_has_calls(
        calls=[
            call(path.join(root_path, dir_name)) for dir_name in walked_directory_names
        ]
    )


def test_get_output_file_path_for_input_file(input_path: str, root_path: str) -> None:
    test_output_path = get_output_file_path_for_input_file(
        input_path=input_path, output_root=root_path
    )

    assert test_output_path == path.join(root_path, input_path + ".md")


@patch("pyremaid.files.destination.makedirs")
@patch("pyremaid.files.destination.path.isdir")
@patch("pyremaid.files.destination.path.dirname")
def test_update_output_file(
    mock_dirname: MagicMock,
    mock_isdir: MagicMock,
    mock_makedirs: MagicMock,
    file_content: str,
    output_file: str,
    output_path: str,
) -> None:
    mock_dirname.return_value = output_path
    mock_isdir.return_value = False

    with patch("pyremaid.files.destination.open", mock_open()) as write_mock:
        update_output_file(content=file_content, output_file=output_file)

    write_mock.assert_called_with(output_file, "w")
    write_mock().write.assert_called_with(file_content)
    mock_dirname.assert_has_calls(calls=[call(output_file), call(output_file)])
    mock_isdir.assert_called_with(output_path)
    mock_makedirs.assert_called_with(output_path)


@patch("pyremaid.files.destination.makedirs")
@patch("pyremaid.files.destination.path.isdir")
@patch("pyremaid.files.destination.path.dirname")
def test_update_output_file_directory_exists(
    mock_dirname: MagicMock,
    mock_isdir: MagicMock,
    mock_makedirs: MagicMock,
    file_content: str,
    output_file: str,
    output_path: str,
) -> None:
    mock_dirname.return_value = output_path
    mock_isdir.return_value = True

    with patch("pyremaid.files.destination.open", mock_open()) as write_mock:
        update_output_file(content=file_content, output_file=output_file)

    write_mock.assert_called_with(output_file, "w")
    write_mock().write.assert_called_with(file_content)
    mock_dirname.assert_called_once_with(output_file)
    mock_isdir.assert_called_with(output_path)
    mock_makedirs.assert_not_called()
