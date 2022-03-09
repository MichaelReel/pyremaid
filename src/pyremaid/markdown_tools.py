
def create_markdown_content(
    input_file: str,
    import_list: list[str],
    debug_dump: str,
) -> str:
    debug_block = create_markdown_debug_dump_block(debug_content=debug_dump)
    import_block = turn_out_the_import_list(import_list=import_list)
    return (
        f"# {input_file}\n\n"
        f"{import_block}\n"
        "---\n"
        "\n"
        f"{debug_block}\n"
    )


def turn_out_the_import_list(import_list: list[str]) -> str:
    list_str = "### Imports\n\n"
    for import_item in import_list:
        list_str += f"  - {import_item}\n"
    return list_str



def create_markdown_debug_dump_block(debug_content: str) -> str:
    return (
        "<details>\n"
        "<summary>Debug AST model dump</summary>\n\n"
        "```\n"
        f"{debug_content}\n"
        "```\n"
        "</details>\n"
    )
