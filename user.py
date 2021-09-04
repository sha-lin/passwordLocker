class User:
    """
    creates new user instances
    """
    pass

    user_array = []

    def __init__(self,full_name,email,mobile_number):
        self.full_name = full_name
        self.email = email
        self.mobile_number = mobile_number

    def save_user_details(self):

        User.user_array.append(self)

    @classmethod
    def display_users(cls):

        return cls.user_array


        pass