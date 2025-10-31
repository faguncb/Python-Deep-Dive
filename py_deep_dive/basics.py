"""
Demonstrates core Python basics:
- Variables and Data Types
- Control Flow (if/else)
- Loops (for/while)
- Functions
- Lambda Functions
"""

def demonstrate_variables():
    """Shows different data types."""
    print("--- Variables & Data Types ---")
    a_int = 10
    a_float = 10.5
    a_str = "Hello"
    a_bool = True
    a_none = None
    print(f"Integer: {a_int} (Type: {type(a_int)})")
    print(f"Float: {a_float} (Type: {type(a_float)})")
    print(f"String: {a_str} (Type: {type(a_str)})")
    print(f"Boolean: {a_bool} (Type: {type(a_bool)})")
    print(f"NoneType: {a_none} (Type: {type(a_none)})")

def demonstrate_control_flow(value):
    """Shows if/elif/else statements."""
    print(f"\n--- Control Flow (Testing value: {value}) ---")
    if value > 50:
        print("Value is greater than 50")
    elif value == 50:
        print("Value is exactly 50")
    else:
        print("Value is less than 50")

def demonstrate_loops():
    """Shows for and while loops."""
    print("\n--- Loops ---")
    print("For loop (0-4):")
    for i in range(5):
        print(f"  i = {i}")

    print("While loop (3-1):")
    count = 3
    while count > 0:
        print(f"  count = {count}")
        count -= 1

# --- Functions ---
# This is a function.
# It takes two integer arguments and returns their sum (an integer).
def add_numbers(x: int, y: int) -> int:
    """Adds two integers together."""
    return x + y

def demonstrate_functions():
    """Shows function calls."""
    print("\n--- Functions ---")
    sum_val = add_numbers(5, 3)
    print(f"add_numbers(5, 3) = {sum_val}")

    # Using keyword arguments
    sum_val_kw = add_numbers(y=10, x=2)
    print(f"add_numbers(y=10, x=2) = {sum_val_kw}")

def demonstrate_lambdas():
    """Shows an example of a lambda function."""
    print("\n--- Lambda Functions ---")
    # A lambda is a small, anonymous function.
    # This is equivalent to:
    # def multiply(x, y):
    #     return x * y
    multiply = lambda x, y: x * y

    print(f"Lambda multiply(5, 5) = {multiply(5, 5)}")

    # Lambdas are often used for sorting
    points = [(1, 2), (4, 1), (3, 5)]
    # Sort by the second element (y-coordinate)
    points.sort(key=lambda p: p[1])
    print(f"Points sorted by y-value: {points}")


def run_demo():
    """Runs all demonstrations in this module."""
    demonstrate_variables()
    demonstrate_control_flow(75)
    demonstrate_loops()
    demonstrate_functions()
    demonstrate_lambdas()
