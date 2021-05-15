"""
Module for testing class Calculator.
"""
import unittest
from unittest import TestCase
from modules.calculator import Calculator


class TestCalculator(TestCase):
    """
    Class for testing calculator.py.
    """

    def setUp(self) -> None:
        """
        Set up calculators for tests.
        """
        self.first_calculator = Calculator(60, 170, 17, 'F', 1.9)
        self.second_calculator = Calculator(80, 180, 25, 'M', 1.2)
        self.third_calculator = Calculator(75, 176, 30, 'M', 1.7)
        self.fourth_calculator = Calculator(55, 160, 24, 'F', 1.5)

    def test_init(self):
        """
        Testing init.
        """
        self.assertEqual(self.first_calculator.weight, 60)
        self.assertEqual(self.second_calculator.age, 25)
        self.assertEqual(self.third_calculator.height, 176)
        self.assertEqual(self.fourth_calculator.activity, 1.5)
        self.assertEqual(self.first_calculator.sex, 'F')

    def test_calories_need(self):
        """
        Testing method calories_need().
        """
        self.assertEqual(self.first_calculator.calories_need(), 2691)
        self.assertEqual(self.second_calculator.calories_need(), 2166)
        self.assertEqual(self.third_calculator.calories_need(), 2898)
        self.assertEqual(self.fourth_calculator.calories_need(), 1904)

    def test_proteins_need(self):
        """
        Testing method proteins_need().
        """
        self.assertEqual(self.first_calculator.proteins_need(), 91)
        self.assertEqual(self.second_calculator.proteins_need(), 77)
        self.assertEqual(self.third_calculator.proteins_need(), 102)
        self.assertEqual(self.fourth_calculator.proteins_need(), 66)

    def test_fats_need(self):
        """
        Testing method fats_need().
        """
        self.assertEqual(self.first_calculator.fats_need(), 90)
        self.assertEqual(self.second_calculator.fats_need(), 72)
        self.assertEqual(self.third_calculator.fats_need(), 97)
        self.assertEqual(self.fourth_calculator.fats_need(), 63)

    def test_carbohydrates_need(self):
        """
        Testing method carbohydrates_need().
        """
        self.assertEqual(self.first_calculator.carbohydrates_need(), 370)
        self.assertEqual(self.second_calculator.carbohydrates_need(), 298)
        self.assertEqual(self.third_calculator.carbohydrates_need(), 398)
        self.assertEqual(self.fourth_calculator.carbohydrates_need(), 262)


if __name__ == '__main__':
    unittest.main()
