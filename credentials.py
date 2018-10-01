import pyperclip
from random import *
import string
from user import User

class Credentials:
    """Class for credentials"""
    credentials_list = []
    def __init__(self,application,username,password):
        """Instantiated credentials"""
        self.application = application
        self.username = username
        self.password = password

    def save_credentials(self):
        """Adding to credentials list"""
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """Remove credentials"""
        Credentials.credentials_list.remove(self)

    def generate_password(self):
        """Generate password """
        min_char = 6
        max_char = 12
        allchar = string.ascii_letters + string.punctuation + string.digits
        pwd = "".join(choice(allchar) for x in range(randint(min_char,max_char)))
        print ("Your new password is:" ,pwd)

    @classmethod
    def credentials_exist(cls, username):
        '''do these credentials exist?'''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        for cred in cls.credentials_list:
            return cred

    @classmethod
    def copy_creds(cls, username):
        creds_to_copy = User.find_user(username)
        pyperclip.copy(creds_to_copy)

"""End of class"""
