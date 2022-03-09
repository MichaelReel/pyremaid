import os
from re import match


def find_all_python_files(input_path: str) -> list[str]:
    python_files = []
    for dirpath, _dirnames, filenames in os.walk(input_path):
        for filename in filenames:
            if match(r".*\.py$", filename):
                python_files.append(os.path.join(dirpath, filename))
    
    return python_files


def get_source_code_from_file(input_file: str) -> str:
    content = ""
    with open(input_file, "r") as md_file:
        content = md_file.read()
    return content


def get_import_name_from_path(input_path: str, input_file: str) -> str:
    return (
        input_file
        .replace(input_path, "")
        .replace(".py", "")
        .replace(".", "")
        .replace(os.sep, ".")
        .replace(".__init__", "")
        .replace("__init__", ".")
    )
