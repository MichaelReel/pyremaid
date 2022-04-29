# pyremaid
Python to Mermaid Diagram (exploration)


No root description quite yet, worth having a look [here](docs/pyremaid/pyremaid.py.md)

Generate markdown documentation with mermaid diagrams for a python project.

## Make commands
For convenience a make file has been provided. Some useful commands are:

| command         | |
| --------------- |-|
| `make run`      | Run the project against the code in the current project
| `make test`     | Run the unittests and display coverage
| `make lint`     | Run the linter against the source files
| `make coverage` | Run unittests and attempt to display coverage in a browser
| `make clean`    | Clear compiled python files and coverage files

If the make commands cannot be used then the following sections will be required:


## Preparation

Install or update to python3.10 or later.

#### Create and use python environment
```sh
python3.10 -m venv ./.env
```
The following is the generic linux shell command, this could be different depending on [Platform and Shell](https://docs.python.org/3/library/venv.html#creating-virtual-environments):
```sh
source ./.env/bin/activate
```

### Install requirements
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

### Executing
```sh
source ./.env/bin/activate
python src/main.py
```

### Testing with coverage
```sh
coverage run --branch -m pytest
coverage html --omit "tests/*"
```

View `htmlcov/index.html` with a browser to view the coverage.

