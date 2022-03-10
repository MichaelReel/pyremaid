
def create_markdown_content(
    input_file: str,
    import_list: list[str],
    global_import_table: dict[str,str],
    mermaid_diagrams: list[str],
    debug_dump: str,
) -> str:
    debug_block = create_markdown_debug_dump_block(debug_content=debug_dump)
    import_block = turn_out_the_import_list(
        import_list=import_list, global_import_table=global_import_table
    )
    mermaid_blocks = "\n".join(mermaid_diagrams)
    return (
        f"# {input_file}\n\n"
        f"{import_block}\n"
        "---\n"
        f"{mermaid_blocks}"
        "---\n"
        "\n"
        f"{debug_block}\n"
    )


def turn_out_the_import_list(
    import_list: list[str], global_import_table: dict[str,str]
) -> str:
    list_str = "### Imports\n\n"
    for import_item in import_list:
        url = global_import_table[import_item]
        if url:
            list_str += f"  - [{import_item}]({url})\n"
        else:
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
