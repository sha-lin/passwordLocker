import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User("Shalin Rono","ronoshalin@gmail.com","0701338496")
    def tearDown(self):

        User.user_array = []

    def test_init(self):

        self.assertEqual(self.new_user.full_name,"Shalin Rono")
        self.assertEqual(self.new_user.email,"ronoshalin@gmail.com")
        self.assertEqual(self.new_user.mobile_number,"0701338496")
                