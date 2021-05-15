"""
Module for testing class Menu.
"""
import unittest
from unittest import TestCase
from modules.menu import Menu


class TestMenu(TestCase):
    """
    Class for testing menu.py.
    """

    def setUp(self) -> None:
        """
        Set up menus for tests.
        """
        self.first_menu = Menu(2000, 70, 60, 300, ['tomato'])
        self.second_menu = Menu(1900, 60, 65, 290, [])

    def tearDown(self) -> None:
        """
        Refreshes menus (makes them empty).
        """
        self.first_menu = Menu(2000, 70, 60, 300, ['tomato'])
        self.second_menu = Menu(1900, 60, 65, 290, [])

    def test_init(self):
        """
        Testing init (it also checks method choose_dishes()).
        """
        self.assertEqual(self.first_menu.calories, 2000)
        self.assertEqual(self.first_menu.proteins, 70)
        self.assertEqual(self.first_menu.fats, 60)
        self.assertEqual(self.first_menu.carbohydrates, 300)
        self.assertEqual(self.first_menu.daily_calories, 0)
        self.assertEqual(self.first_menu.daily_fats, 0)
        self.assertEqual(self.first_menu.daily_proteins, 0)
        self.assertEqual(self.first_menu.daily_carbohydrates, 0)
        self.assertEqual(len(self.first_menu.all_dishes), 6580)
        self.assertEqual(len(self.second_menu.all_dishes), 7344)

    def test_menu(self):
        """
        Testing methods __str__(), generate_menu(), accept_dish(), generate_dish() and delete_dish().
        """
        self.assertEqual(self.first_menu.__str__(), '')
        self.first_menu.generate_menu()
        self.assertNotEqual(self.first_menu.__str__(), '')
        self.assertEqual(len(self.first_menu.menu), 3)
        self.assertTrue(0.85*self.first_menu.calories <= self.first_menu.menu[0].calories +
                        self.first_menu.menu[1].calories + self.first_menu.menu[2].calories <= 1.15*self.first_menu.calories)
        self.assertTrue(0.85*self.first_menu.proteins <= self.first_menu.menu[0].proteins +
                        self.first_menu.menu[1].proteins + self.first_menu.menu[2].proteins <= 1.15*self.first_menu.proteins)
        self.assertTrue(0.85*self.first_menu.fats <= self.first_menu.menu[0].fats +
                        self.first_menu.menu[1].fats + self.first_menu.menu[2].fats <= 1.15*self.first_menu.fats)
        self.assertTrue(0.85*self.first_menu.carbohydrates <= self.first_menu.menu[0].carbohydrates +
                        self.first_menu.menu[1].carbohydrates + self.first_menu.menu[2].carbohydrates <= 1.15*self.first_menu.carbohydrates)
        self.first_menu.accept_dish(self.first_menu.menu[0])
        self.assertTrue(self.first_menu.daily_calories <=
                        0.4*self.first_menu.calories)
        self.assertTrue(self.first_menu.daily_proteins <=
                        0.4*self.first_menu.proteins)
        self.assertTrue(self.first_menu.daily_fats <=
                        0.4*self.first_menu.calories)
        self.assertTrue(self.first_menu.daily_fats <=
                        0.4*self.first_menu.carbohydrates)
        self.first_menu.accept_dish(self.first_menu.menu[1])
        self.assertTrue(0.5*self.first_menu.calories <= self.first_menu.daily_calories <=
                        0.9*self.first_menu.calories)
        self.assertTrue(0.5*self.first_menu.proteins <= self.first_menu.daily_proteins <=
                        0.9*self.first_menu.proteins)
        self.assertTrue(0.5*self.first_menu.fats <= self.first_menu.daily_fats <=
                        0.9*self.first_menu.fats)
        self.assertTrue(0.5*self.first_menu.carbohydrates <= self.first_menu.daily_carbohydrates <=
                        0.9*self.first_menu.carbohydrates)
        self.first_menu.accept_dish(self.first_menu.menu[2])
        self.assertTrue(0.85*self.first_menu.calories <=
                        self.first_menu.daily_calories <= 1.15*self.first_menu.calories)
        self.assertTrue(0.85*self.first_menu.proteins <=
                        self.first_menu.daily_proteins <= 1.15*self.first_menu.proteins)
        self.assertTrue(0.85*self.first_menu.fats <=
                        self.first_menu.daily_fats <= 1.15*self.first_menu.fats)
        self.assertTrue(0.85*self.first_menu.carbohydrates <=
                        self.first_menu.daily_carbohydrates <= 1.15*self.first_menu.carbohydrates)
        self.second_menu.generate_menu()
        self.second_menu.delete_dish(self.second_menu.menu[2])
        self.second_menu.accept_dish(self.second_menu.menu[0])
        self.second_menu.accept_dish(self.second_menu.menu[1])
        self.second_menu.accept_dish(self.second_menu.menu[2])
        self.assertTrue(0.85*self.first_menu.calories <=
                        self.first_menu.daily_calories <= 1.15*self.first_menu.calories)
        self.assertTrue(0.85*self.first_menu.proteins <=
                        self.first_menu.daily_proteins <= 1.15*self.first_menu.proteins)
        self.assertTrue(0.85*self.first_menu.fats <=
                        self.first_menu.daily_fats <= 1.15*self.first_menu.fats)
        self.assertTrue(0.85*self.first_menu.carbohydrates <=
                        self.first_menu.daily_carbohydrates <= 1.15*self.first_menu.carbohydrates)

    def test_product(self):
        """
        Testing methods search_product(), choose_product().
        """
        self.assertEqual(len(self.first_menu.search_product('tomato')), 50)
        self.assertEqual(
            len(self.second_menu.search_product('mango juice')), 50)
        self.first_menu.choose_product('tomatoes, raw', 100)
        self.assertAlmostEqual(self.first_menu.daily_calories, 18.0)
        self.assertAlmostEqual(self.first_menu.daily_proteins, 0.88)
        self.assertAlmostEqual(self.first_menu.daily_fats, 0.2)
        self.assertAlmostEqual(self.first_menu.daily_carbohydrates, 3.89)
        self.first_menu.choose_product('mango nectar', 150)
        self.assertAlmostEqual(self.first_menu.daily_calories, 94.5)
        self.assertAlmostEqual(self.first_menu.daily_proteins, 1.045)
        self.assertAlmostEqual(self.first_menu.daily_fats, 0.29)
        self.assertAlmostEqual(self.first_menu.daily_carbohydrates, 23.54)


if __name__ == '__main__':
    unittest.main()
