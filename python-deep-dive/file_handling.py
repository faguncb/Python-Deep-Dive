"""
Demonstrates File I/O and Error Handling:
- Writing to a file using 'with'
- Reading from a file
- Handling exceptions (try/except/finally)
"""
import os

FILE_NAME = "demo_file.txt"

def write_demo_file():
    """Writes text to a file using the 'with' statement."""
    print(f"--- Writing to {FILE_NAME} ---")
    # The 'with' statement is the preferred way to open files.
    # It automatically handles closing the file, even if errors occur.
    # 'w' mode = write (overwrites the file if it exists)
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            f.write("Hello, this is line 1.\n")
            f.write("This is line 2.\n")
            f.write("And this is line 3.\n")
        print("File written successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")

def read_demo_file():
    """Reads text from a file."""
    print(f"\n--- Reading from {FILE_NAME} ---")
    # 'r' mode = read (default mode)
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            # Read the whole file at once
            # content = f.read()
            # print("Full content:\n", content)

            # Or read line by line (more memory efficient for large files)
            print("Reading line by line:")
            for line in f:
                print(f"  > {line.strip()}") # .strip() removes newline characters

    except FileNotFoundError:
        print(f"Error: The file '{FILE_NAME}' was not found.")
    except IOError as e:
        print(f"Error reading file: {e}")

def demonstrate_error_handling(value):
    """Demonstrates a try/except/finally block."""
    print(f"\n--- Error Handling (Dividing 10 by {value}) ---")
    try:
        # Code that might fail
        result = 10 / value
        print(f"Result: {result}")
    except ZeroDivisionError:
        # Handle a *specific* error
        print("Error: Cannot divide by zero.")
    except TypeError:
        # Handle another specific error
        print("Error: Invalid type. Must be a number.")
    except Exception as e:
        # A general catch-all for any other exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        # This block *always* runs, whether an error
        # occurred or not. Useful for cleanup.
        print("Finally block executed.")

def cleanup_file():
    """Removes the demo file."""
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print(f"\nCleaned up {FILE_NAME}.")

def run_demo():
    """Runs all demonstrations in this module."""
    write_demo_file()
    read_demo_file()

    demonstrate_error_handling(2)    # Success
    demonstrate_error_handling(0)    # ZeroDivisionError
    demonstrate_error_handling("a")  # TypeError

    cleanup_file()
