Python Deep Dive Project
This project is a comprehensive, framework-free Python application designed to demonstrate key aspects of the Python programming language, standard project structure, testing, and CI/CD.
Project Structure
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


How to Use This Project
1. Setup
   Clone the repository and create a virtual environment:
   git clone <your-repo-url>
   cd Python-Deep-Dive
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
This project's main code has no external dependencies, but we need pytest for testing.
pip install -r requirements.txt


2. Run the Main Code
   The main.py file is configured to run demonstrations from all modules.
   python3 main.py


3. Run Tests
   We use pytest to discover and run all tests in the tests/ directory.
   pytest


You can also run with coverage:
pytest --cov=py_deep_dive


4. Build the Project
   You can build this project into a wheel (.whl) file, which is a standard way to distribute Python packages.
   python3 setup.py sdist bdist_wheel


This will create a dist/ folder with your package file.
5. Deploy with Docker
   The Dockerfile provides a way to "deploy" this project as a self-contained image.
   Build the image:
   docker build -t python-deep-dive .


Run the image:
This will run the main.py script from within the container.
docker run python-deep-dive


6. Maintain (CI/CD)
   The .github/workflows/main.yml file will automatically run on every push or pull_request to your repository on GitHub. It will:
   Set up Python.
   Install dependencies.
   Run pytest to ensure all tests pass.
   This ensures that new code doesn't break existing functionality.
