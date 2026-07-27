#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for testing max_integer function."""

    def test_max_at_end(self):
        """Test with max integer at the end of list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max integer at the beginning of list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with max integer in the middle of list."""
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_negative(self):
        """Test list with one negative number."""
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_all_negative(self):
        """Test list with all negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        """Test list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_default_empty(self):
        """Test with no arguments passed."""
        self.assertEqual(max_integer(), None)

    def test_float_numbers(self):
        """Test list with float numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_ints_and_floats(self):
        """Test list with integers and floats."""
        self.assertEqual(max_integer([1.5, 2, 3.5, 1]), 3.5)

    def test_string(self):
        """Test with a string input."""
        self.assertEqual(max_integer("hello"), 'o')


if __name__ == '__main__':
    unittest.main()
