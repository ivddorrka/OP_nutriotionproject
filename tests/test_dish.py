"""
Module for testing class Dish.
"""
import unittest
from unittest import TestCase
from modules.dish import Dish


class TestDish(TestCase):
    """
    Class for testing dish.py.
    """

    def setUp(self) -> None:
        """
        Set up dish for tests.
        """
        self.dish = Dish(
            'pasta', 'prepare', '1 pack of pasta', 300, 5, 10, 60)

    def test_init(self):
        """
        Testing init.
        """
        self.assertEqual(self.dish.name, 'pasta')
        self.assertEqual(self.dish.products, '1 pack of pasta')
        self.assertEqual(self.dish.proteins, 5)
        self.assertEqual(self.dish.calories, 300)
        self.assertEqual(self.dish.carbohydrates, 60)
        self.assertEqual(self.dish.fats, 10)
        self.assertEqual(self.dish.instruction, 'prepare')


if __name__ == '__main__':
    unittest.main()
