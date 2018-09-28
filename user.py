class User:
    """Generates user class and all its behaviours"""
    user_list = []

    def __init__(self,first_name,second_name):
        self.first_name = first_name
        self.second_name = second_name

    def save_user(self):
        """Adds new users"""
        User.user_list.append(self)

    def delete_user(self):
        """remove a user"""
        User.user_list.remove(self)

    @classmethod
    def find_user(cls,first_name):
        """Finds user by first name"""
        for user in cls.user_list:
            if user.first_name == first_name:
                return user