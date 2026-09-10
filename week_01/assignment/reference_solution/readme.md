# Week 1 Reference Solution

This directory contains the executable companion code for the instructor
solution deck. It establishes a validated grid-problem abstraction and an
extensible agent interface. It intentionally contains no search algorithm.

## Requirements

- Python 3.10 or newer
- NumPy
- JupyterLab
- Git

## Verification

From this directory, run:

```text
python verify_environment.py
python -m unittest discover -s tests -v
```

The environment check also requires the directory to be inside a Git work tree
with at least one commit.

