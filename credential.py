class Credential:
    pass
    credentials_array = []

    def __init__(self,user_name,password,email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credentials(self):

        Credential.credentials_array.append(self)

    @classmethod
    def display_credentials(cls):

        return cls.credentials_array    