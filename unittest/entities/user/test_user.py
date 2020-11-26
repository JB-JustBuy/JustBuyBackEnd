import unittest
from src.model.user import User


class TestUser(unittest.TestCase):
    def test_validate_format(self):
        data = {
            "username": 'testusername001',
            'email': 'testusername001@gmail.com',
            'password': "testpassword001",
            'confirmPassword': 'testpassword001'
        }
        res = User.validate_format(data)
        self.assertEqual([], res)

    def test_validate_username(self):
        username = 't1'
        self.assertEqual("length of username needs to bigger than 6", User.validate_username(username)[0])

        username = '%3tsete1'
        self.assertEqual("username cant use symbol", User.validate_username(username)[0])

        username = "%1"
        res = User.validate_username(username)
        self.assertTrue("username cant use symbol" in res)
        self.assertTrue('length of username needs to bigger than 6' in res)
        #
        username = 'testuser001'
        self.assertTrue(User.validate_username(username) == [])

    def test_validate_email(self):
        email = "0001"
        self.assertEqual("email format error", User.validate_email(email)[0])

        email = "0222.com.tw"
        self.assertEqual("email format error", User.validate_email(email)[0])

        email = 'testusername001@gmail.com'
        self.assertTrue(User.validate_email(email) == [])

    def test_validate_password(self):
        password = '100'
        self.assertEqual("length of password needs to bigger than 8", User.validate_password(password)[0])

        password = '3r232rafax'
        self.assertTrue(User.validate_password(password) == [])

    def test_validate_confirm_password(self):
        password = "000"
        confirm_password = '111'
        self.assertEqual("password and confirm password arent the same",
                         User.validate_confirm_password(password, confirm_password)[0])

        confirm_password = '000'
        self.assertTrue(User.validate_confirm_password(password, confirm_password) == [])