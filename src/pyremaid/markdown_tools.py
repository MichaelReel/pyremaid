
def create_markdown_content(input_file: str, debug_dump: str) -> str:
    debug_block = create_markdown_debug_dump_block(debug_content=debug_dump)
    return (
        f"# {input_file}\n"
        "\n"
        f"{debug_block}\n"
    )


def create_markdown_debug_dump_block(debug_content: str) -> str:
    return (
        "<details>\n"
        "<summary>Debug AST model dump</summary>\n\n"
        "```\n"
        f"{debug_content}\n"
        "```\n"
        "</details>\n"
    )
