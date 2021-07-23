# Some Root Factors

- Python packages are installed globally by default
- `pip` doesn't handle dependency resolution well
  - Pip 20.3 has a new dependency resolver, but it is unclear exactly which dependency related problems it solves. (https://pip.pypa.io/en/latest/user_guide/#changes-to-the-pip-dependency-resolver-in-20-3-2020)
- `pip uninstall` removes the package, but doesn't remove its dependencies.
- Can't use `requirements.txt` for your top level dependencies if you also want to `pip freeze`.
- pip doesn't have a lock file.

- Poetry provides a lock file and reproducible builds

- List of a few things Poetry provides
  - https://news.ycombinator.com/item?id=25253236

Transitive dependencies:
https://medium.com/knerd/the-nine-circles-of-python-dependency-hell-481d53e3e025

- Package A depends on Package C version 0.2.5
- Package B depends on Package C version 1.0.1
Poetry handles it.

See https://muttdata.ai/blog/2020/08/21/a-poetic-apology.html for a full background of the problems that Poetry solves.



# Poetry

## Usage

### 1. Set your config to have your virtual env inside your project dir, rather than in the Poetry default location of `~Library/Caches/pypoetry/virtualenvs`

`poetry config --local virtualenvs.in-project true`

Creates `poetry.toml` with contents:
```toml
[virtualenvs]
in-project = true
```

### 2. Create your Poetry project

`poetry init`

Creates your `pyproject.toml` file

### 3. Create your virtual env and lock file

`poetry install`

Creates
- Your virtual env dir `.venv` (per the config in `poetry.toml`)
- `poetry.lock`

### 4. Install a package

`poetry add PACKAGE_NAME`

# Examples

## Example 1

`python example1.py`

Why did it work?

## Example 2

`python example2.py`

`poetry add numpy`

`poetry run python example2.py`
