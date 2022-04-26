from os import path
from pytest import fixture

from pyremaid.models import MermaidElement


@fixture
def global_import_table() -> dict[str, str]:
    return {"import 1": "mapped import 1", "import 2": None}


@fixture
def input_path() -> str:
    return "input path"


@fixture
def input_file(input_path: str) -> str:
    return path.join(input_path, "input file name")


@fixture
def output_path() -> str:
    return "output path"


@fixture
def output_file(output_path: str) -> str:
    return path.join(output_path, "output file name")


@fixture
def root_path() -> str:
    # TODO: Need to get clear on how this is used compared to output_path
    #       and probably consider how path variables are named across the project
    return "root"


file_content_data = (  # Appeasing the mock_open (I don't like this)
    "mocked up file content"
)


@fixture
def file_content() -> str:
    return file_content_data


@fixture
def walked_directory_names() -> list[str]:
    return ["dirnames"]


@fixture
def walked_file_names() -> list[str]:
    return [
        "python_file.py",
        "non_python_file.txt",
        "more_python.py",
        "py.but_not.py.pyc",
    ]


@fixture
def walked_files(
    root_path: str,
    walked_directory_names: list[str],
    walked_file_names: list[str],
) -> list[tuple[str, list[str], list[str]]]:
    return [(root_path, walked_directory_names, walked_file_names)]


@fixture
def no_mermaid_elements() -> list[MermaidElement]:
    return []


@fixture
def no_elements_graph() -> str:
    return "```mermaid\n" "flowchart TB\n" "\n" "\n" "```\n"
