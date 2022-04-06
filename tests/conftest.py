from pytest import fixture


@fixture
def global_import_table() -> dict[str, str]:
    return {"import 1": "mapped import 1", "import 2": None}


@fixture
def input_path() -> str:
    return "input path"


@fixture
def input_file() -> str:
    return "input file name"


@fixture
def output_path() -> str:
    return "output path"
