.PHONY: run test lint coverage clean

VENV = .env
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
COVERAGE = $(VENV)/bin/coverage
PYTHON_VERSION = 3.10

$(VENV)/bin/activate: requirements.txt
	python$(PYTHON_VERSION) -m venv $(VENV)
	$(PIP) install -r requirements.txt

init: $(VENV)/bin/activate;

run: init
	$(PYTHON) src/main.py

test: init
	$(COVERAGE) run --branch -m pytest
	$(COVERAGE) report --omit "tests/*"

lint: init
	$(VENV)/bin/black .
	$(VENV)/bin/flake8 --ignore=E501 --exclude=$(VENV) .

coverage: init
	$(COVERAGE) run --branch -m pytest
	$(COVERAGE) html --omit "tests/*"
	xdg-open htmlcov/index.html

clean:
	rm -rf htmlcov
	rm -f .coverage
	rm -rf .pytest_cache
	find . -type d -name __pycache__ -exec rm -r {} \+
	rm -rf $(VENV)

 