import unittest
import pyperclip
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''runs before each test case'''
        self.new_credentials = Credentials("insta", "kevahere", "3nd0fDay5")

    def test_init(self):
        self.assertEqual(self.new_credentials.username, "kevahere")
        self.assertEqual(self.new_credentials.password, "3nd0fDay5")
        self.assertTrue(self.new_credentials.application, "Insta")

    def tearDown(self):
        Credentials.credentials_list = []

    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)