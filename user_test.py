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

    def test_save_user(self):

        self.new_user.save_user_details()
        self.assertEqual(len(User.user_array), 1)    

    def test_save_multiple_users(self):

        self.new_user.save_user_details()
        test_user = User("Test", "user", "user@gmail.com", "0701338496") 
        test_user.save_user_details()
        self.assertEqual(len(User.user_array), 2) 

    def test_display_all_users(self):

        self.assertEqual(User.display_users(), User.user_array)      
                