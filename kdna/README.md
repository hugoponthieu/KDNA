# KDNA

This is the official repository for the DO2023-2026 python CLI backup project

## Init for dev

After cloning the repo you will need to install all dependencies

### Lancer la commande KDNA

```bash
# python kdna/main.py
```

### Obtenir les informations nécessaires à l'utilisation de chaque commande

```bash
# python kdna/main.py <commande> --help
# python kdna/main.py <commande> <sous-commande> --help
```

## Usage


### Lancer un autobackup
```bash
python kdna/main.py autobackup
```

### Sauvegarder un fichier
```bash
python kdna/main.py backup
```

### Choisir un serveur
```bash
python kdna/main.py server
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
