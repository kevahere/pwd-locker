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
        """Generate """
