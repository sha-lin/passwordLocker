import unittest
from credential import Credential

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_credential = Credential("user_name", "password","email@gmail.com")
        