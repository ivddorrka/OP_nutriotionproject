"""
Module for testing class User.
"""
import unittest
from modules.user import PasswordTooShortError, User


class TestUser(unittest.TestCase):
    """
    Class for testing user.py.
    """

    def setUp(self):
        """
        Set up user for tests.
        """
        self.user = User('example_person')
        self.user2 = User('another_user')

    def test_set_password(self):
        """
        Testing method set_password.
        """
        with self.assertRaises(PasswordTooShortError):
            self.user.set_password('1234')
            self.user.set_password('')
            self.user.set_password('1234567')
        self.user.set_password('password')
        self.assertEqual(self.user.password, 'password')

    def test_get_age(self):
        """
        Testing method get_age.
        """
        with self.assertRaises(ValueError):
            self.user.get_age('seventeen')
            self.user.get_age('')
            self.user.get_age('dkjghg')

    def test_get_height(self):
        """
        Testing method get_height.
        """
        with self.assertRaises(ValueError):
            self.user.get_height('hundred')
            self.user.get_height('')
            self.user.get_height('idk')
            self.user.get_height('hundred')
            self.user.get_height([])

    def test_get_weight(self):
        """
        Testing method get_weight.
        """
        with self.assertRaises(ValueError):
            self.user.get_weight('sixty')
            self.user.get_weight('')
            self.user.get_weight('dghshgf')
            self.user.get_weight([])

    def test_get_activ(self):
        """
        Testing method get_activ.
        """
        with self.assertRaises(ValueError):
            self.user.get_activ('one')
            self.user.get_activ('')
            self.user.get_activ('little 56')
            self.user.get_activ([])

    def test_set_gender(self):
        """
        Testing method set_gender.
        """
        self.user.set_gender('male')
        self.assertTrue(self.user.gender == 'male')

    def test_set_characteristic(self):
        """
        Testing method set_characteristics.
        """
        with self.assertRaises(ValueError):
            self.user2.set_characteristics(
                'twenty', 164, 60, 'male', '1.0 - little')
            self.user2.set_characteristics(
                20, 'tall', 60, 'male', '1.3 - some info')
            self.user2.set_characteristics(
                20, 160, 'heavy', 'male', '1.4 - lots')
            self.user2.set_characteristics(
                20, 160, 65, 'male', 'none')
        self.user2.set_characteristics(20, 170, 64, 'female', '1.5 - info')
        self.assertEqual(self.user2.age, 20)
        self.assertEqual(self.user2.height, 170)
        self.assertEqual(self.user2.weight, 64)
        self.assertEqual(self.user2.gender, 'female')
        self.assertEqual(self.user2.activity, 1.5)


if __name__ == "__main__":
    unittest.main()
