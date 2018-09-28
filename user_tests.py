import unittest
from user import User

class TestUser(unittest.TestCase):
    '''Test class for user behaviour'''

    def setUp(self):
        """Checking the user is instantiated correctly"""
        self.new_user = User("Kevin","Ahere")

    def test_init(self):
        """Checking for the proper init"""
        self.assertEqual(self.new_user.first_name,"Kevin")
        self.assertEqual(self.new_user.second_name,"Ahere")



