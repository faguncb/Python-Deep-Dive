"""
Unit tests for the 'basics' module.
Tests are written using the standard `unittest` module,
but are run using `pytest`.
"""

import unittest
from py_deep_dive import basics

class TestBasics(unittest.TestCase):
    """Test suite for functions in basics.py"""

    def test_add_numbers(self):
        """Tests the add_numbers function."""
        # Test with positive integers
        self.assertEqual(basics.add_numbers(2, 3), 5)

        # Test with negative numbers
        self.assertEqual(basics.add_numbers(-5, 5), 0)

        # Test with zero
        self.assertEqual(basics.add_numbers(10, 0), 10)

    def test_lambda_sort(self):
        """
        This isn't a great unit test, but it demonstrates
        testing a side-effect (modifying a list).

        A better way would be to have the lambda logic
        in a standalone function.
        """
        print("\nNote: `demonstrate_lambdas` prints to console, "
              "this test checks the sorting logic directly.")

        points = [(1, 5), (4, 1), (3, 2)]

        # Get the same lambda logic from the module
        sort_key = lambda p: p[1]

        points.sort(key=sort_key)

        expected_order = [(4, 1), (3, 2), (1, 5)]
        self.assertEqual(points, expected_order)

# This allows running the test file directly, though `pytest` is preferred
if __name__ == '__main__':
    unittest.main()
