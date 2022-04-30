from ast import AST
from os import path
from pytest import fixture

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
def mermaid_node() -> MermaidNode:
    return MermaidNode(
        ast_node=AST(),
        mermaid_safe_name="safe_name",
        display_name="display_name",
    )


@fixture
def linked_mermaid_node() -> MermaidNode:
    return MermaidNode(
        ast_node=AST(),
        mermaid_safe_name="other_safe_name",
        display_name="other_display_name",
    )


@fixture
def mermaid_link(
    mermaid_node: MermaidNode, linked_mermaid_node: MermaidNode
) -> MermaidLink:
    return MermaidLink(from_=mermaid_node, to=linked_mermaid_node)


@fixture
def mermaid_backlink(
    linked_mermaid_node: MermaidNode, mermaid_node: MermaidNode
) -> MermaidLink:
    return MermaidLink(from_=linked_mermaid_node, to=mermaid_node)


@fixture
def mermaid_block() -> MermaidBlock:
    return MermaidBlock(
        ast_node=AST(),
        mermaid_safe_name="safe_name",
        display_name="display_name",
    )


@fixture
def mermaid_module() -> MermaidModule:
    return MermaidModule(
        ast_node=AST(),
        mermaid_safe_name="safe_name",
        display_name="display_name",
    )


@fixture
def mermaid_function() -> MermaidFunction:
    return MermaidFunction(
        ast_node=AST(),
        mermaid_safe_name="safe_name",
        display_name="display_name",
    )


@fixture
def mermaid_class() -> MermaidClass:
    return MermaidClass(
        ast_node=AST(),
        mermaid_safe_name="safe_name",
        display_name="display_name",
    )


@fixture
def mermaid_for() -> MermaidFor:
    return MermaidFor(
        ast_node=AST(),
        mermaid_safe_name="safe_name",
        display_name="display_name",
    )


@fixture
def mermaid_elements(
    mermaid_node: MermaidNode,
    mermaid_link: MermaidLink,
    mermaid_backlink: MermaidLink,
    mermaid_block: MermaidBlock,
    mermaid_module: MermaidModule,
    mermaid_function: MermaidFunction,
    mermaid_class: MermaidClass,
    mermaid_for: MermaidFor,
) -> list[MermaidElement]:
    return [
        mermaid_node,
        mermaid_link,
        mermaid_backlink,
        mermaid_block,
        mermaid_module,
        mermaid_function,
        mermaid_class,
        mermaid_for,
    ]


@fixture
def no_elements_graph() -> str:
    return "```mermaid\n" "flowchart TB\n" "\n" "\n" "```\n"


@fixture
def node_graph() -> str:
    return "```mermaid\n" "flowchart TB\n" "\n" "\n" "```\n"


@fixture
def link_graph() -> str:
    return (
        "```mermaid\n"
        "flowchart TB\n"
        '  safe_name["display_name"]\n'
        '  other_safe_name["other_display_name"]\n'
        "\n"
        "  safe_name --> other_safe_name\n"
        "\n"
        "```\n"
    )


@fixture
def block_graph() -> str:
    return "```mermaid\n" "flowchart TB\n" "\n" "\n" "```\n"


@fixture
def module_graph() -> str:
    return "```mermaid\n" "flowchart TB\n" "\n" "\n" "```\n"


@fixture
def function_graph() -> str:
    return (
        "```mermaid\n"
        "flowchart TB\n"
        "\n"
        "  subgraph display_name\n"
        "    direction TB\n"
        "  end\n"
        "\n"
        "```\n"
    )


@fixture
def class_graph() -> str:
    return (
        "```mermaid\n"
        "flowchart TB\n"
        "\n"
        "  subgraph display_name\n"
        "    direction TB\n"
        "  end\n"
        "\n"
        "```\n"
    )


@fixture
def for_graph() -> str:
    return (
        "```mermaid\n"
        "flowchart TB\n"
        "\n"
        "  %% loop display_name\n"
        "  %% end display_name\n"
        "\n"
        "```\n"
    )


@fixture
def elements_graph() -> str:
    return (
        "```mermaid\n"
        "flowchart TB\n"
        '  safe_name["display_name"]\n'
        '  other_safe_name["other_display_name"]\n'
        "\n"
        "  safe_name --> other_safe_name\n"
        "  other_safe_name --> safe_name\n"
        "  subgraph display_name\n"
        "    direction TB\n"
        "  end\n"
        "  subgraph display_name\n"
        "    direction TB\n"
        "  end\n"
        "  %% loop display_name\n"
        "  %% end display_name\n"
        "\n"
        "```\n"
    )
