import unittest
import pyperclip
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''runs before each test case'''
        self.new_credentials = Credentials("insta", "kevahere", "3nd0fDay5")