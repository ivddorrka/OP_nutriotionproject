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
        self.menu = Menu(2000, 70, 60, 300, ['tomato'])

    def test_init(self):
        """
        Testing init.
        """
        self.assertEqual(self.menu.calories, 2000)
        self.assertEqual(self.menu.proteins, 2000)
        self.assertEqual(self.menu.fats, 2000)
        self.assertEqual(self.menu., 2000)
        self.assertEqual(self.menu.calories, 2000)
