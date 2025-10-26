"""
Main entry point for the py_deep_dive project.

This script imports functions and classes from the various modules
within the 'py_deep_dive' package and executes them to demonstrate
their functionality.
"""

# Importing from our package
from py_deep_dive import basics
from py_deep_dive import data_structures
from py_deep_dive import oop
from py_deep_dive import file_handling
from py_deep_dive import standard_lib

def main():
    """Main function to run all demonstrations."""
    print("--- 1. Running Basics Demo ---")
    basics.run_demo()
    print("\n" + "="*30 + "\n")

    print("--- 2. Running Data Structures Demo ---")
    data_structures.run_demo()
    print("\n" + "="*30 + "\n")

    print("--- 3. Running OOP Demo ---")
    oop.run_demo()
    print("\n" + "="*30 + "\n")

    print("--- 4. Running File Handling Demo ---")
    file_handling.run_demo()
    print("\n" + "="*30 + "\n")

    print("--- 5. Running Standard Library Demo ---")
    standard_lib.run_demo()
    print("\n" + "="*30 + "\n")

    print("--- All Demos Complete ---")

if __name__ == "__main__":
    # This block ensures that main() is called only when
    # this script is executed directly (not when imported as a module).
    main()
