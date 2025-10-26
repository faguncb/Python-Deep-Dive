# Project Structure

```
Python-Deep-Dive/
│
├── .github/
│   └── workflows/
│       └── main.yml        # CI pipeline (lint, test, build)
│
├── docs/
│   └── OOPS.md             # Documentation for OOP concepts
│
├── py_deep_dive/
│   ├── __init__.py         # Makes 'py_deep_dive' a Python package
│   ├── basics.py           # Variables, control flow, functions, lambdas
│   ├── data_structures.py  # Lists, dicts, sets, tuples, comprehensions
│   ├── file_handling.py    # File I/O, 'with' statement, error handling
│   ├── oop.py              # Classes, inheritance, polymorphism, etc.
│   └── standard_lib.py     # Examples using 'json' and 'datetime'
│
├── tests/
│   ├── __init__.py         # Makes 'tests' a Python package
│   ├── test_basics.py      # Unit tests for basics.py
│   └── test_oop.py         # Unit tests for oop.py
│
├── .gitignore              # Files to ignore in Git
├── Dockerfile              # Containerizes the application
├── main.py                 # Main entry point to run demonstrations
├── requirements.txt        # Project dependencies (for testing/linting)
└── setup.py                # Build script for the package (using setuptools)
```
