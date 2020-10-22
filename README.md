## Requirements:
1. Project is running with python 3.8+
2. [Poetry](https://python-poetry.org/docs/) is required to work with dependencies



## Set up project:

1. Clone your reposiotory:
```sh
git clone git@github.com:szewczykmira/spotiweekly.git
```
2. Enter the repository and create virtualenv with python 3.8
```sh
cd spotiweekly
mkvirtualenv -p python3.8 spotiweekly
```
3. **[Optional]** you can update project's name in `pyproject.toml`
4. Install dependencies
```sh
poetry install
```
5. Install pre-commit hooks
```sh
pre-commit install
```


## Running tests
```sh
make test
```

- running test with checking test coverage
```sh
pytest --cov={repository_name} tests/
```

## Running application
```sh
make run 
```
