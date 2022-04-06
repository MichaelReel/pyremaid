from os import walk, path, sep
from re import match


def find_all_python_files(input_path: str) -> list[str]:
    python_files = []
    for dirpath, _dirnames, filenames in walk(input_path):
        for filename in filenames:
            if match(r".*\.py$", filename):
                python_files.append(path.join(dirpath, filename))

    return python_files


def get_source_code_from_file(input_file: str) -> str:
    content = ""
    with open(input_file, "r") as md_file:
        content = md_file.read()
    return content


def get_import_name_from_path(input_path: str, input_file: str) -> str:
    """
    Attempt to figure out the module path from the python file name
    Input_path is the root path and input_file is the full python file path

    This _relies_ on the sanity of the input parameters

    String input_path off the input_file, remove `.py`, remove `.`,
    change file separator to `.`, remove `.__init__`,
    replace `__init__` with `.`
    """
    # Might be someway to use importlib to do this
    return (
        input_file.replace(input_path, "")
        .replace(".py", "")
        .replace(".", "")
        .replace(sep, ".")
        .replace(".__init__", "")
        .replace("__init__", ".")
    )
