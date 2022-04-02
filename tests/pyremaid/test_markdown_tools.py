from pytest import fixture
from unittest.mock import MagicMock, patch

from pyremaid.markdown_tools import (
    create_markdown_content,
    turn_out_the_import_list,
    create_markdown_debug_dump_block,
)


@fixture
def input_file() -> str:
    return "input file name"


@fixture
def import_list() -> list[str]:
    return ["import 1", "import 2"]


@fixture
def mermaid_diagrams() -> list[str]:
    return ["diagram 1", "diagram 2"]


@fixture
def debug_dump() -> str:
    return "debug dump"


@fixture
def mermaid_block(mermaid_diagrams: list[str]) -> str:
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
def import_list_block() -> str:
    return "### Imports\n\n  - [import 1](mapped import 1)\n  - import 2\n"


@fixture
def expected_markdown(
    input_file: str,
    import_list_block: str,
    mermaid_block: str,
    debug_dump_block: str,
) -> str:
    return (
        f"# {input_file}\n\n"
        f"{import_list_block}\n"
        "---\n"
        f"{mermaid_block}"
        "---\n"
        "\n"
        f"{debug_dump_block}\n"
    )


@patch("pyremaid.markdown_tools.create_markdown_debug_dump_block")
@patch("pyremaid.markdown_tools.turn_out_the_import_list")
def test_create_markdown_content(
    mock_turn_out_the_import_list: MagicMock,
    mock_create_markdown_debug_dump_block: MagicMock,
    import_list_block: str,
    debug_dump_block: str,
    input_file: str,
    import_list: list[str],
    global_import_table: dict[str, str],
    mermaid_diagrams: list[str],
    debug_dump: str,
    expected_markdown: str,
) -> None:
    mock_turn_out_the_import_list.return_value = import_list_block
    mock_create_markdown_debug_dump_block.return_value = debug_dump_block

    test_markdown = create_markdown_content(
        input_file=input_file,
        import_list=import_list,
        global_import_table=global_import_table,
        mermaid_diagrams=mermaid_diagrams,
        debug_dump=debug_dump,
    )

    mock_turn_out_the_import_list.assert_called_with(
        import_list=import_list, global_import_table=global_import_table
    )
    mock_create_markdown_debug_dump_block.assert_called_with(debug_content=debug_dump)

    assert test_markdown == expected_markdown


def test_turn_out_the_import_list(
    import_list: list[str], global_import_table: dict[str, str], import_list_block: str
) -> None:
    test_imports_output = turn_out_the_import_list(
        import_list=import_list, global_import_table=global_import_table
    )
    assert test_imports_output == import_list_block


def test_create_markdown_debug_dump_block(
    debug_dump: str, debug_dump_block: str
) -> None:
    test_debug_dump_block = create_markdown_debug_dump_block(debug_dump)
    assert test_debug_dump_block == debug_dump_block
