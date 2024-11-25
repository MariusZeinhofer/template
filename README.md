# Template

A minimal Python template using pytest and ruff. To configure this template change
``template'' to the chosen project name in the following locations:

- -conda_env.yaml in line 1
- pyproject.toml in line 2
- in this README in line 16

## Setup Conda Environment

You can set up the `conda` environment and activate it

```bash
conda env create --file .conda_env.yaml
conda activate template
```

## No Conda: Editable Install with PIP

In case you are not using conda you can install the package 
in editable mode using:

```bash
pip install -e ."[lint,test]"
```

## Linting and Formatting

We use ruff for linting and formatting:

```bash
ruff check .
ruff format .
```