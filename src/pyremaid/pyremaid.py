#!/usr/bin/env python3

import os


def create_mermaid_from_python(input_path : str, output_path :str):
    for dirname, dirnames, filenames in os.walk(input_path):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            print(os.path.join(dirname, filename))

        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if '.git' in dirnames:
            # don't go into any .git directories.
            dirnames.remove('.git')


if __name__ == "__main__":
    # Assume we want to run against the current directory
    input_path = "."
    output_path = "./docs/pyremaid/"
    create_mermaid_from_python(input_path=input_path, output_path=output_path)
