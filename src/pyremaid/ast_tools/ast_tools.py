from ast import AST, dump, parse
from typing import Optional

from ast_tools.visitors import ImportNodeFinder


def get_ast_root_node_for_file(source_code: str, input_file: str) -> Optional[AST]:
    return parse(
        source=source_code,
        filename=input_file,
        mode='exec',
        type_comments=True,
    )


def get_markdown_dump_for_ast_node(ast_node: AST) -> str:
    return dump(ast_node, annotate_fields=True, include_attributes=True, indent=2)


def get_used_import_list(ast_node: AST) -> list[str]:
    finder = ImportNodeFinder()
    finder.visit(ast_node)
    return finder.get_found_imports()
