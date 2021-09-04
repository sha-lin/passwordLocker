from user import User
from credential import Credential


def create_user(fullname,email,mobilenumber):

    new_user = User(fullname,email,mobilenumber)
    return new_user


def create_credential(username, psword, email):

    new_credential = Credential(username,psword,email)
    return new_credential    