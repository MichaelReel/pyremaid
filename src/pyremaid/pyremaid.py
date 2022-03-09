#!/usr/bin/env python3

from files.destination import (
    create_cleared_output_folder,
    get_output_file_path_for_input_file,
    update_output_file,
)
from files.source import find_all_python_files, get_source_code_from_file, get_import_name_from_path
from ast_tools import get_ast_root_node_for_file, get_markdown_dump_for_ast_node, get_used_import_list
from ast_tools.import_map import get_all_imports_from_files
from markdown_tools import create_markdown_content

def create_mermaid_analysis_from_python(input_path : str, output_path :str):
    create_cleared_output_folder(output_path=output_path)
    python_files = find_all_python_files(input_path=input_path)
    global_import_list = get_all_imports_from_files(input_path=input_path, python_files=python_files)

    print("\n".join([f"{k}: {v}" for k,v in global_import_list.items()]))

    for in_file in python_files:
        out_file = get_output_file_path_for_input_file(
            input_path=in_file, output_root=output_path
        )

        debug_dump = ""
        import_list = []

        if source_code := get_source_code_from_file(input_file=in_file):
            if ast_node := get_ast_root_node_for_file(
                source_code=source_code,
                input_file=in_file,
            ):
                # Get basic AST debug, we can include on the page in a reveal block
                debug_dump = get_markdown_dump_for_ast_node(ast_node=ast_node)
                # Get the imports used in this file
                import_list = get_used_import_list(ast_node=ast_node)


        
        markdown_content = create_markdown_content(
            input_file=in_file,
            import_list=import_list, # Not useful yet, still debug
            debug_dump=debug_dump
        )

        update_output_file(content=markdown_content, output_file=out_file)


if __name__ == "__main__":
    # "Assume" we want to run against the current project
    # Need to make this configurable (of course)
    input_path = "./src/pyremaid/"
    output_path = "./docs/pyremaid/"
    create_mermaid_analysis_from_python(input_path=input_path, output_path=output_path)
