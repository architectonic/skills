---
name: Python Packaging
description: Create distributable Python packages with proper project structure, pyproject.toml, and publishing to PyPI. Use when packaging Python libraries, creating CLI tools, or distributing Python code.
source: SWE-Skills-Bench (SWE-Skills-Bench/skills/python-packaging/SKILL.md)
license: MIT
tags: [software-development, python, packaging, pypi, pyproject-toml, distribution, cli]
type: Playbook
---

# Python Packaging

Create, structure, and distribute Python packages using modern packaging tools and pyproject.toml.

## When to Use This Skill

- Creating Python libraries for distribution
- Building command-line tools with entry points
- Publishing packages to PyPI or private repositories
- Setting up Python project structure

## Core Concepts

### Package Structure

- **Source layout**: `src/package_name/` (recommended)
- **Flat layout**: `package_name/` (simpler but less flexible)
- **Build backends**: setuptools, hatchling, flit, poetry
- **Distribution formats**: wheel (.whl) and source distribution (.tar.gz)

### Modern Packaging Standards

- **PEP 517/518**: Build system requirements
- **PEP 621**: Metadata in pyproject.toml
- **PEP 660**: Editable installs

## Quick Start

### Minimal Package Structure

```
my-package/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── module.py
└── tests/
    └── test_module.py
```

### Minimal pyproject.toml

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my-package"
version = "0.1.0"
description = "A short description"
authors = [{name = "Your Name", email = "you@example.com"}]
readme = "README.md"
requires-python = ">=3.8"
dependencies = ["requests>=2.28.0"]

[project.optional-dependencies]
dev = ["pytest>=7.0", "black>=22.0"]
```

## Key Patterns

### Source Layout (Recommended)

```
my-package/
├── pyproject.toml
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core.py
│       └── py.typed
└── tests/
    └── test_core.py
```

```toml
[tool.setuptools.packages.find]
where = ["src"]
```

### Full-Featured pyproject.toml

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-awesome-package"
version = "1.0.0"
description = "An awesome Python package"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [{name = "Your Name", email = "you@example.com"}]
classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]
dependencies = [
    "requests>=2.28.0,<3.0.0",
    "click>=8.0.0",
]

[project.optional-dependencies]
dev = ["pytest>=7.0.0", "black>=23.0.0", "ruff>=0.1.0"]

[project.urls]
Homepage = "https://github.com/username/my-awesome-package"
Repository = "https://github.com/username/my-awesome-package"

[project.scripts]
my-cli = "my_package.cli:main"

[tool.setuptools.packages.find]
where = ["src"]
include = ["my_package*"]
```

### Dynamic Versioning

```toml
[build-system]
requires = ["setuptools>=61.0", "setuptools-scm>=8.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my-package"
dynamic = ["version"]

[tool.setuptools_scm]
write_to = "src/my_package/_version.py"
```

### CLI with Click

```python
# src/my_package/cli.py
import click

@click.group()
@click.version_option()
def cli():
    """My awesome CLI tool."""
    pass

@cli.command()
@click.argument("name")
@click.option("--greeting", default="Hello", help="Greeting to use")
def greet(name: str, greeting: str):
    click.echo(f"{greeting}, {name}!")

def main():
    cli()
```

```toml
[project.scripts]
my-tool = "my_package.cli:main"
```

### Build and Publish

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Check the distribution
twine check dist/*

# Test on TestPyPI first
twine upload --repository testpypi dist/*

# Publish to PyPI
twine upload dist/*
```

### Automated Publishing with GitHub Actions

```yaml
# .github/workflows/publish.yml
name: Publish to PyPI
on:
  release:
    types: [created]

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - run: pip install build twine
      - run: python -m build
      - run: twine check dist/*
      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

### Including Data Files

```toml
[tool.setuptools.package-data]
my_package = ["data/*.json", "templates/*.html", "py.typed"]
```

```python
from importlib.resources import files

def load_config():
    config_file = files("my_package").joinpath("data/config.json")
    with config_file.open() as f:
        return json.load(f)
```

### Editable Install and Testing

```bash
# Install in development mode
pip install -e .

# With optional dependencies
pip install -e ".[dev]"

# Test in isolated environment
python -m venv test-env
source test-env/bin/activate
pip install dist/my_package-1.0.0-py3-none-any.whl
python -c "import my_package; print(my_package.__version__)"
```

## Version Management

```toml
# Semantic versioning: MAJOR.MINOR.PATCH
# MAJOR: Breaking changes
# MINOR: New features (backward compatible)
# PATCH: Bug fixes

# Version constraints:
dependencies = [
    "requests>=2.28.0,<3.0.0",  # Compatible range
    "click~=8.1.0",              # Compatible release
    "pydantic>=2.0",             # Minimum version
]
```

## Checklist for Publishing

- [ ] Code is tested (pytest passing)
- [ ] Documentation is complete (README, docstrings)
- [ ] Version number updated
- [ ] CHANGELOG.md updated
- [ ] License file included
- [ ] pyproject.toml is complete
- [ ] Package builds without errors
- [ ] Installation tested in clean environment
- [ ] CLI tools work (if applicable)
- [ ] PyPI metadata is correct (classifiers, keywords)
- [ ] Tested on TestPyPI first
- [ ] Git tag created for release

## Best Practices

1. **Use src/ layout** for cleaner package structure
2. **Use pyproject.toml** for modern packaging
3. **Pin build dependencies** in build-system.requires
4. **Version appropriately** with semantic versioning
5. **Include all metadata** (classifiers, URLs, etc.)
6. **Test installation** in clean environments
7. **Use TestPyPI** before publishing to PyPI
8. **Document thoroughly** with README and docstrings
9. **Include LICENSE** file
10. **Automate publishing** with CI/CD

## Resources

- **Python Packaging Guide**: https://packaging.python.org/
- **PyPI**: https://pypi.org/
- **TestPyPI**: https://test.pypi.org/
