from os import makedirs, path, remove, rmdir, walk


def _create_output_folder(output_path: str) -> None:
    if not path.isdir(output_path):
        makedirs(output_path)


def create_cleared_output_folder(output_path: str) -> None:
    _create_output_folder(output_path=output_path)
    for root, dirs, files in walk(output_path, topdown=False):
        for name in files:
            remove(path.join(root, name))
        for name in dirs:
            rmdir(path.join(root, name))


def get_output_file_path_for_input_file(input_path: str, output_root: str) -> str:
    return path.join(output_root, input_path + ".md")


def update_output_file(content: str, output_file: str) -> None:
    if not path.isdir(path.dirname(output_file)):
        makedirs(path.dirname(output_file))

    with open(output_file, "w") as md_file:
        md_file.write(content)
