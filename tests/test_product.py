"""
Module for testing class Product.
"""
import unittest
from unittest import TestCase
from modules.product import Product


class TestProduct(TestCase):
    """
    Class for testing product.py.
    """

    def setUp(self) -> None:
        """
        Set up products for tests.
        """
        self.first_product = Product('tomato')
        self.second_product = Product('mango juice')

    def test_init(self):
        """
        Testing init.
        """
        self.assertEqual(self.first_product.name, 'tomato')
        self.assertEqual(self.second_product.name, 'mango juice')

    def test_get_products(self):
        """
        Testing method get_products().
        """
        self.assertEqual(len(self.first_product.get_products()), 50)
        self.assertEqual(len(self.second_product.get_products()), 50)

    def test_choose_product(self):
        """
        Testing method choose_product().
        """
        self.assertTupleEqual(self.first_product.choose_product('tomatoes, raw', 100),
                              (18.0, 0.88, 0.2, 3.89))
        self.assertTupleEqual(self.first_product.choose_product('tomatoes, raw', 200),
                              (36.0, 1.76, 0.4, 7.78))
        self.assertTupleEqual(self.second_product.choose_product('mango nectar', 150),
                              (76.5, 0.165, 0.09, 19.65))


if __name__ == '__main__':
    unittest.main()
