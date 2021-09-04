import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User("Shalin Rono","ronoshalin@gmail.com","0701338496")