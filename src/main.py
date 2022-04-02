#!/usr/bin/env python3

from pyremaid.pyremaid import create_mermaid_analysis_from_python

if __name__ == "__main__":
    # "Assume" we want to run against the current project
    # Need to make this configurable (of course)
    input_path = "./src/pyremaid/"
    output_path = "./docs/pyremaid/"
    create_mermaid_analysis_from_python(input_path=input_path, output_path=output_path)
