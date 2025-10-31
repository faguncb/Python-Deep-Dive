"""
Unit tests for the 'oop' module.
"""

import unittest
import math
from py_deep_dive.oop import Circle, Rectangle, print_shape_area, Shape

class TestOOP(unittest.TestCase):
    """Test suite for classes in oop.py"""

    def setUp(self):
        """
        This method runs before each test.
        It's a good place to create objects that
        will be used in multiple tests.
        """
        self.circle = Circle(radius=10, color="blue")
        self.rectangle = Rectangle(width=10, height=5, color="yellow")

    def test_circle_creation(self):
        """Test that the Circle is initialized correctly."""
        self.assertEqual(self.circle.get_radius(), 10)
        self.assertEqual(self.circle.get_color(), "blue")

    def test_rectangle_creation(self):
        """Test that the Rectangle is initialized correctly."""
        self.assertEqual(self.rectangle.width, 10)
        self.assertEqual(self.rectangle.height, 5)
        self.assertEqual(self.rectangle.get_color(), "yellow")

    def test_circle_area(self):
        """Test the Circle's area calculation (Polymorphism)."""
        expected_area = math.pi * (10**2)
        self.assertAlmostEqual(self.circle.area(), expected_area)

    def test_rectangle_area(self):
        """Test the Rectangle's area calculation (Polymorphism)."""
        self.assertEqual(self.rectangle.area(), 50)

    def test_encapsulation_setter(self):
        """Test the Circle's radius setter and validation."""
        self.circle.set_radius(20)
        self.assertEqual(self.circle.get_radius(), 20)

        # Test that setting a negative radius raises a ValueError
        # This is how you test for expected exceptions
        with self.assertRaises(ValueError):
            self.circle.set_radius(-5)

    def test_abstraction(self):
        """Test that the base Shape class raises a NotImplementedError."""
        s = Shape()
        with self.assertRaises(NotImplementedError):
            s.area()

    def test_polymorphism_duck_typing(self):
        """
        This tests the `print_shape_area` function.
        Since that function prints to stdout, we would
        need to mock stdout to test it properly.

        For simplicity, we'll just test that the objects
        have the 'area' method, which is what the
        function relies on (duck typing).
        """
        self.assertTrue(hasattr(self.circle, "area"))
        self.assertTrue(hasattr(self.rectangle, "area"))

if __name__ == '__main__':
    unittest.main()
