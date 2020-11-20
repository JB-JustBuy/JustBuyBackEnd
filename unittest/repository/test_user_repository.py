from src.repository.user_respository import UserRepository
import unittest


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_rp = UserRepository({
            "database": 'just_buy',
            'collection': 'users'
        })

        self.data = {
            "username": 'testusername001',
            'email': 'testusername001@gmail.com',
            'password': "testpassword001",
            'confirmPassword': 'testpassword001'
        }
        self.user_rp.write(data={"document": self.data})

    def tearDown(self):
        self.user_rp.delete(data={'query':self.data})

    def test_exist_in_repositeory(self):
        data = {
            "username": 'testusername001',
            'email': 'testuseranme002@gmail.com',
            'password': "testpassword001",
            'confirmPassword': 'testpassword001'
        }
        self.assertEqual('This username has been used', self.user_rp._UserRepository__is_exist(data))

        data = {
            "username": 'testusername002',
            'email': 'testusername001@gmail.com',
            'password': "testpassword001",
            'confirmPassword': 'testpassword001'
        }
        self.assertEqual('This email has registered', self.user_rp._UserRepository__is_exist(data))

    def test_validate_format(self):
        data = {
            "username": 'testusername001',
            'email': 'testusername001@gmail.com',
            'password': "testpassword001",
            'confirmPassword': 'testpassword001'
        }
        res = self.user_rp.validate_format(data)
        self.assertEqual("success", res['status'])

    def test_validate_username(self):
        username = 't1'
        self.assertEqual("length of username needs to bigger than 6", self.user_rp._UserRepository__validate_username(username)[0])

        username = '%3tsete1'
        self.assertEqual("username cant use symbol", self.user_rp._UserRepository__validate_username(username)[0])

        username = "%1"
        res = self.user_rp._UserRepository__validate_username(username)
        self.assertTrue("username cant use symbol" in res)
        self.assertTrue('length of username needs to bigger than 6' in res)
        #
        username = 'testuser001'
        print(self.user_rp._UserRepository__validate_username(username))
        self.assertTrue(self.user_rp._UserRepository__validate_username(username) == [])

    def test_validate_email(self):
        email = "0001"
        self.assertEqual("email format error", self.user_rp._UserRepository__validate_email(email)[0])

        email = "0222.com.tw"
        self.assertEqual("email format error", self.user_rp._UserRepository__validate_email(email)[0])

        email = '001@gmail.com'
        self.assertTrue(self.user_rp._UserRepository__validate_email(email) == [])

    def test_validate_password(self):
        password = '100'
        self.assertEqual("length of password needs to bigger than 8", self.user_rp._UserRepository__validate_password(password)[0])

        password = '3r232rafax'
        self.assertTrue(self.user_rp._UserRepository__validate_password(password) == [])

    def test_validate_confirm_password(self):
        password = "000"
        confirm_password = '111'
        self.assertEqual("password and confirm password arent the same",
                        self.user_rp._UserRepository__validate_confirm_password(password, confirm_password)[0])

        confirm_password = '000'
        self.assertTrue(self.user_rp._UserRepository__validate_confirm_password(password, confirm_password) == [])