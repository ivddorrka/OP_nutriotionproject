"""
Module for testing class UserDB.
"""
import unittest
from modules.user import User
from modules.user_db import UserNotFound, UserAlreadyExists, UserDB


class TestUserDB(unittest.TestCase):
    """
    Class for testing user_db.py.
    """

    def setUp(self):
        """
        Set up users and user_db for tests.
        """
        self.user_db = UserDB()

        self.mariya = User('mariya')
        self.oleg = User('oleg')
        self.david = User('david')
        self.ustyna = User('ustyna')

    def test_add(self):
        """
        Testing method add.
        """
        self.user_db.add(self.mariya)
        self.assertTrue(self.mariya in self.user_db.users)
        self.user_db.add(self.oleg)
        self.assertTrue(self.oleg in self.user_db.users)
        self.user_db.add(self.david)
        self.assertTrue(self.david in self.user_db.users)
        self.assertTrue(self.user_db.users == [
                        self.mariya, self.oleg, self.david])
        with self.assertRaises(UserAlreadyExists):
            self.user_db.add(self.david)

    def test_get(self):
        """
        Testing method get.
        """
        self.user_db.add(self.mariya)
        self.user_db.add(self.oleg)
        self.user_db.add(self.david)
        self.assertEqual(self.user_db.get('david'), self.david)
        self.assertEqual(self.user_db.get('oleg'), self.oleg)
        self.assertEqual(self.user_db.get('mariya'), self.mariya)
        with self.assertRaises(UserNotFound):
            self.user_db.get('sofiia')
            self.user_db.get('oleg1')
            self.user_db.get('tetyana')

    def test_pop(self):
        """
        Testing method pop.
        """
        self.user_db.add(self.mariya)
        self.user_db.add(self.oleg)
        self.user_db.add(self.david)
        with self.assertRaises(UserNotFound):
            self.user_db.get('sofiia')
            self.user_db.get('oleg1')
            self.user_db.get('tetyana')
            self.user_db.get(self.ustyna)
            self.user_db.get(User('no_name'))
        popped_user = self.user_db.pop('david')
        self.assertTrue(popped_user not in self.user_db.users)
        self.assertTrue(popped_user == self.david)
        popped_user = self.user_db.pop('oleg')
        self.assertTrue(popped_user not in self.user_db.users)
        self.assertTrue(popped_user == self.oleg)
        popped_user = self.user_db.pop('mariya')
        self.assertTrue(popped_user not in self.user_db.users)
        self.assertTrue(popped_user == self.mariya)

    def test_clear(self):
        """
        Testing method clear.
        """
        self.user_db.add(self.mariya)
        self.user_db.add(self.oleg)
        self.user_db.add(self.david)
        self.user_db.clear()
        self.assertTrue(len(self.user_db.users) == 0)

    def test_str(self):
        """
        Testing str.
        """
        self.user_db.add(self.mariya)
        self.user_db.add(self.oleg)
        self.user_db.add(self.david)
        user_db_str = 'UserDB(mariya, oleg, david)'
        self.assertEqual(str(self.user_db), user_db_str)


if __name__ == "__main__":
    unittest.main()
