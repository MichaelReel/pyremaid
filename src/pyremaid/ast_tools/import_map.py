from pyremaid.ast_tools import get_ast_root_node_for_file, get_used_import_list
from pyremaid.files.source import get_source_code_from_file, get_import_name_from_path


def _get_import_to_file_map(input_path: str, python_files: list[str]) -> dict[str, str]:
    """Create a mapping of import paths to filenames first"""
    import_to_file_map = {}

    for in_file in python_files:
        import_name = get_import_name_from_path(
            input_path=input_path, input_file=in_file
        )
        import_to_file_map[import_name] = in_file

    return import_to_file_map


def _get_parent_import(import_name: str) -> str:
    return import_name[: import_name.rfind(".")]


def _create_import_table(
    python_files: list[str], import_to_file_map: dict[str, str]
) -> dict[str, str]:

    all_imports_table = {}

    for in_file in python_files:
        if source_code := get_source_code_from_file(input_file=in_file):
            if ast_node := get_ast_root_node_for_file(
                source_code=source_code,
                input_file=in_file,
            ):
                for used_import in get_used_import_list(ast_node=ast_node):
                    known_file = ""
                    parent_import = _get_parent_import(used_import)
                    if parent_import in import_to_file_map:
                        known_file = import_to_file_map[parent_import]
                    all_imports_table[used_import] = known_file

    return all_imports_table


def get_all_imports_from_files(
    input_path: str, python_files: list[str]
) -> dict[str, str]:
    """
    This is kind of expensive for what it does
    It's tricky not to require multiple passes to achieve what is being done here
    """

    import_to_file_map = _get_import_to_file_map(
        input_path=input_path, python_files=python_files
    )

    all_imports_table = _create_import_table(
        python_files=python_files, import_to_file_map=import_to_file_map
    )

    return all_imports_table
