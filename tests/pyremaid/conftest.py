from pytest import fixture


@fixture
def global_import_table() -> dict[str, str]:
    return {"import 1": "mapped import 1", "import 2": None}
