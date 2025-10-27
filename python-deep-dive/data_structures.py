"""
Demonstrates core Python data structures:
- Lists
- Tuples
- Dictionaries
- Sets
- Comprehensions (List, Dict)
"""

def demonstrate_lists():
    """Shows list creation, indexing, slicing, and methods."""
    print("--- Lists (Mutable, Ordered) ---")
    fruits = ["apple", "banana", "cherry"]
    print(f"Initial list: {fruits}")

    # Add an item
    fruits.append("orange")
    print(f"After append: {fruits}")

    # Indexing (0-based)
    print(f"First item: {fruits[0]}")
    # Slicing [start:stop:step]
    print(f"Middle items: {fruits[1:3]}")
    # Negative indexing
    print(f"Last item: {fruits[-1]}")

def demonstrate_tuples():
    """Shows tuple creation and immutability."""
    print("\n--- Tuples (Immutable, Ordered) ---")
    # Tuples are created with parentheses
    point = (10, 20, 30)
    print(f"Point tuple: {point}")

    # They can be "unpacked"
    x, y, z = point
    print(f"Unpacked: x={x}, y={y}, z={z}")

    # This would cause a TypeError:
    # point[0] = 5

def demonstrate_dictionaries():
    """Shows dictionary creation, item access, and iteration."""
    print("\n--- Dictionaries (Mutable, Unordered <3.7, Ordered 3.7+) ---")
    # Key-Value pairs
    user = {
        "name": "Alice",
        "age": 30,
        "is_admin": False
    }
    print(f"User dict: {user}")

    # Access items by key
    print(f"User's name: {user['name']}")

    # Add/Update item
    user["age"] = 31
    user["email"] = "alice@example.com"
    print(f"Updated user: {user}")

    # Iterate over items
    print("Iterating over user:")
    for key, value in user.items():
        print(f"  {key}: {value}")

def demonstrate_sets():
    """Shows set creation, uniqueness, and operations."""
    print("\n--- Sets (Mutable, Unordered, Unique Items) ---")
    numbers = {1, 2, 3, 3, 4, 2, 5}
    print(f"Set (duplicates removed): {numbers}")

    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    # Set operations
    print(f"Union (A | B): {set_a | set_b}")
    print(f"Intersection (A & B): {set_a & set_b}")
    print(f"Difference (A - B): {set_a - set_b}")

def demonstrate_comprehensions():
    """Shows list and dictionary comprehensions."""
    print("\n--- Comprehensions (A concise way to create lists/dicts) ---")

    # List comprehension: squares of numbers 0-9
    squares = [x**2 for x in range(10)]
    print(f"Squares list: {squares}")

    # List comprehension with condition: even squares
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Even squares: {even_squares}")

    # Dictionary comprehension
    names = ["Alice", "Bob", "Charlie"]
    name_lengths = {name: len(name) for name in names}
    print(f"Name lengths dict: {name_lengths}")

def run_demo():
    """Runs all demonstrations in this module."""
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dictionaries()
    demonstrate_sets()
    demonstrate_comprehensions()
