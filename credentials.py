import pyperclip
import random
import string

class Credentials:
    """Class for credentials"""
    credentials_list = []
    def __init__(self,application,username,password):
        """Instantiated credentials"""
        self.application = application
        self.username
        self.password

    def save_credentials:
        """Adding to credentials list"""
        Credentials.credentials_list.append(self)

    def delete_credentials:
        """Remove credentials"""
        Credentials.credentials_list.remove()

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

