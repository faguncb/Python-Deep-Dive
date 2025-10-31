"""
Demonstrates Object-Oriented Programming (OOP) concepts:
- Classes and Objects
- Constructor (__init__)
- Methods
- Inheritance
- Encapsulation (using '_' and '__')
- Polymorphism (Duck Typing and Method Overriding)
"""
import math

# --- Abstraction (Base Class) ---
# We define an "abstract" idea of what a Shape is.
# Real classes will inherit from this and implement 'area'.
class Shape:
    """Abstract base class for a shape."""
    def __init__(self):
        # This is a "protected" attribute, convention says
        # it shouldn't be accessed directly from outside.
        self._color = "blue"

    def area(self):
        """Calculates the area of the shape."""
        # This is a placeholder. Subclasses *should* override this.
        # This is a form of Abstraction.
        raise NotImplementedError("Subclass must implement abstract method")

    def get_color(self):
        """Public getter for the protected color attribute."""
        return self._color

# --- Inheritance & Encapsulation ---

class Circle(Shape):
    """
    A Circle class that inherits from Shape.
    Demonstrates: Inheritance, Encapsulation, Method Overriding.
    """
    def __init__(self, radius, color="red"):
        # Call the parent's constructor
        super().__init__()

        # Override the protected attribute
        self._color = color

        # This is a "private" attribute, indicated by two underscores.
        # Python "name-mangles" this to _Circle__radius to avoid
        # conflicts with subclasses.
        self.__radius = radius

    def get_radius(self):
        """Public getter for the private radius."""
        return self.__radius

    def set_radius(self, radius):
        """Public setter with validation (Encapsulation)."""
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = radius

    # --- Polymorphism (Method Overriding) ---
    def area(self):
        """Calculates the area of the circle."""
        # We override the 'area' method from the parent 'Shape' class.
        return math.pi * (self.__radius ** 2)

    def __str__(self):
        """String representation of the object."""
        return f"{self.get_color().capitalize()} Circle with radius {self.__radius}"

class Rectangle(Shape):
    """A Rectangle class that inherits from Shape."""
    def __init__(self, width, height, color="green"):
        super().__init__()
        self._color = color
        self.width = width
        self.height = height

    # --- Polymorphism (Method Overriding) ---
    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def __str__(self):
        """String representation of the object."""
        return f"{self.get_color().capitalize()} Rectangle (w={self.width}, h={self.height})"


# --- Polymorphism (Duck Typing) ---
# This function doesn't care about the *type* of object (Circle, Rectangle).
# It only cares if the object has an .area() method.
# "If it walks like a duck and quacks like a duck, it's a duck."
def print_shape_area(shape):
    """Prints the area of any object that has an .area() method."""
    # This is Polymorphism in action.
    # The same function `print_shape_area` works for different objects
    # that share an interface (the `area` method).
    print(f"Object: {shape}")
    print(f"  Area: {shape.area():.2f}")


def run_demo():
    """Runs all demonstrations in this module."""
    print("--- Classes & Objects ---")
    c1 = Circle(10, color="purple")
    r1 = Rectangle(5, 10)

    print(c1)
    print(r1)

    print("\n--- Encapsulation Demo ---")
    print(f"Circle radius (via getter): {c1.get_radius()}")
    # This will fail with an AttributeError:
    # print(c1.__radius)

    # Using the setter
    c1.set_radius(12)
    print(f"Circle radius (after setter): {c1.get_radius()}")

    try:
        c1.set_radius(-5)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("\n--- Polymorphism Demo ---")
    shapes = [c1, r1]

    for shape in shapes:
        print_shape_area(shape)
