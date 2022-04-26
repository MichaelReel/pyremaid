#!/usr/bin/env python3

from pyremaid.pyremaid import create_mermaid_analysis_from_python


def main():
    # "Assume" we want to run against the current project
    # Need to make this configurable (of course)
    input_path = "./src/"
    output_path = "./docs/"
    create_mermaid_analysis_from_python(input_path=input_path, output_path=output_path)


if __name__ == "__main__":  # pragma: no cover
    main()
