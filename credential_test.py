import unittest
from credential import Credential

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_credential = Credential("user_name", "password","email@gmail.com")

    def tearDown(self):

        Credential.credentials_array = []

    def test_init(self):

        self.assertEqual(self.new_credential.user_name, "user_name")
        self.assertEqual(self.new_credential.password, "password")
        self.assertEqual(self.new_credential.email, "email@gmail.com")

    def test_save_cred(self):

        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credentials_array), 1)

    def test_display_credentials(self):

        self.assertEqual(Credential.display_credentials(), Credential.credentials_array)

if __name__ == '__main__':
    unittest.main()

