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
def ast() -> AST:
    return AST()


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


@fixture
def no_python_files() -> list[str]:
    return []


@fixture
def empty_imports_table() -> dict[str, str]:
    return {}


@fixture
def python_files() -> list[str]:
    return ["python file 1", "python file 2"]


@fixture
def import_list() -> list[str]:
    return ["import A", "import B"]


@fixture
def global_import_table(import_list: list[str]) -> dict[str, str]:
    return {import_list[0]: "mapped import 1", import_list[1]: None}


@fixture
def all_imports_table(import_list: list[str]) -> dict[str, str]:
    return {
        import_list[0]: "",
        import_list[1]: "",
    }


@fixture
def mermaid_element_list() -> list[MermaidElement]:
    return [MermaidElement(), MermaidElement()]


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
def resolved_python_files(root_path: str) -> list[str]:
    return [
        path.join(root_path, "python_file.py"),
        path.join(root_path, "more_python.py"),
    ]


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
def linked_mermaid_node(ast: AST) -> MermaidNode:
    return MermaidNode(
        ast_node=ast,
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


@fixture
def mermaid_diagrams() -> list[str]:
    return ["diagram 1", "diagram 2"]


@fixture
def debug_dump() -> str:
    return "debug dump"


@fixture
def mermaid_diagram_block(mermaid_diagrams: list[str]) -> str:
    return "\n".join(mermaid_diagrams)


@fixture
def debug_dump_block(debug_dump: str) -> str:
    return (
        "<details>\n"
        "<summary>Debug AST model dump</summary>\n\n"
        "```\n"
        f"{debug_dump}\n"
        "```\n"
        "</details>\n"
    )


@fixture
def import_list_block(import_list: list[str]) -> str:
    return f"### Imports\n\n  - [{import_list[0]}](mapped import 1)\n  - {import_list[1]}\n"


@fixture
def expected_markdown(
    input_file: str,
    import_list_block: str,
    mermaid_diagram_block: str,
    debug_dump_block: str,
) -> str:
    return (
        f"# {input_file}\n\n"
        f"{import_list_block}\n"
        "---\n"
        f"{mermaid_diagram_block}"
        "---\n"
        "\n"
        f"{debug_dump_block}\n"
    )
