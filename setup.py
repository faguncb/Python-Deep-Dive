from setuptools import setup, find_packages

setup(
    name="py_deep_dive",
    version="0.1.0",
    description="A project to demonstrate core Python concepts",
    author="Fagun Bhavsar",
    author_email="fagun.bhavsar@gmail.com",

    # find_packages() automatically finds all packages (directories with __init__.py)
    packages=find_packages(where="."),

    # This tells setuptools that the package code is in the root directory
    # If our code was in a 'src' folder, we would use: package_dir={"": "src"}

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',

    # This package itself has no dependencies, but if it did,
    # they would be listed here, e.g.:
    # install_requires=[
    #     "requests>=2.0.0",
    # ],

    # This specifies the entry point for the console script
    # After installing this package (`pip install .`), you could just run `run-demo`
    entry_points={
        "console_scripts": [
            "run-demo=main:main",
        ],
    },
)
