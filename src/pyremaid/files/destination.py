import os


def create_output_folder(output_path : str) -> None:
    if not os.path.isdir(output_path):
        os.makedirs(output_path)


def create_cleared_output_folder(output_path: str) -> None:
    create_output_folder(output_path=output_path)
    for root, dirs, files in os.walk(output_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def get_output_file_path_for_input_file(input_path: str, output_root: str) -> str:
    return os.path.join(output_root, input_path + ".md")


def update_output_file(content: str, output_file: str):
    if not os.path.isdir(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))

    with open(output_file, "w") as md_file:
        md_file.write(content)

