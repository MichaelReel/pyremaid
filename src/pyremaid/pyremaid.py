#!/usr/bin/env python3

from files.destination import (
    create_cleared_output_folder,
    get_output_file_path_for_input_file,
    update_output_file,
)
from files.source import find_all_python_files, get_source_code_from_file
from ast_tools import get_ast_root_node_for_file, get_markdown_dump_for_ast_node
from markdown_tools import create_markdown_content

def create_mermaid_analysis_from_python(input_path : str, output_path :str):
    create_cleared_output_folder(output_path=output_path)
    python_files = find_all_python_files(input_path=input_path)

    for in_file in python_files:
        out_file = get_output_file_path_for_input_file(
            input_path=in_file, output_root=output_path
        )

        debug_dump = ""

        if source_code := get_source_code_from_file(input_file=in_file):
            if ast_node := get_ast_root_node_for_file(
                source_code=source_code,
                input_file=in_file,
            ):
                debug_dump = get_markdown_dump_for_ast_node(ast_node=ast_node)
        
        markdown_content = create_markdown_content(
            input_file=in_file,
            debug_dump=debug_dump
        )

        update_output_file(content=markdown_content, output_file=out_file)


if __name__ == "__main__":
    # "Assume" we want to run against the current directory
    input_path = "."
    output_path = "./docs/pyremaid/"
    create_mermaid_analysis_from_python(input_path=input_path, output_path=output_path)
