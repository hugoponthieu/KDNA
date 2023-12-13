# KDNA

This is the official repository for the DO2023-2026 python CLI backup project

## Init for dev

After cloning the repo you will need to install all dependencies

```bash
# install deps
poetry install
```

## Usage


### Start the app
```bash
poetry run python KDNA/__init__.py
```
### Run the tests
```bash
poetry run pytest
```
### Run the pipeline
```bash
poetry run tox
```
```bash
#run the pipeline with a specific env
poetry run tox -e (env)
```
### Build the documentation
```bash
sphinx-apidoc -f -o docs/source kdna/
sphinx-build -M html docs/source/ docs/build/
```

## Package added
    - click             # Parseur
    - fabric            # SSH client
    - pycryptodome      # Encrypt tool
    - pylint            # Linter
    - mypy              # Type checker
    - pytest            # Test framework
    - tox               # Test runner
    - tox-gh-actions    # Tox github action
    - sphinx            # Documentation generator
    - sphinx-rtd-theme  # Read the docs theme
    - sphinx-autoapi    # Auto documentation generator
    - m2r2              # Markdown to reStructuredText converter
    - pydocstyle        # Docstring style checker
    - chardet           # Encoding detector

### Contributeur :
    - Dorian Grasset : mise en place du système de sécurité concernant le CRUD des serveurs & backups (100%)
    - Benoit Planche : mise en place du CRUD (https://github.com/somoslosdorados/KDNA/tree/POC-5-BPL)
    - Mathias Durat & Tristan Radulescu : relecteur
