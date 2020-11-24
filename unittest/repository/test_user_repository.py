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


    def test_get_users(self):
        users = self.user_rp.get_users()
        print(users)

    def test_add_user(self):
        user1 = self.data
        res = self.user_rp.signup(user1)
        self.assertEqual('failed', res['status'])
        self.assertEqual(2, len(res['message']))


        user2 = {
            'username': 'testusername002',
            'email': 'testusername002@gmail.com',
            'password': 'sae22v777',
            'confirmPassword': 'sae22v777'
        }
        res = self.user_rp.signup(user2)
        self.assertEqual('success', res['status'])
        self.assertEqual([], res['message'])

    def test_exist_in_repository(self):
        data = {
            "username": 'testusername001',
            'email': 'testuseranme002@gmail.com',
            'password': "testpassword001",
            'confirmPassword': 'testpassword001'
        }
        self.assertEqual('This username has been used', self.user_rp.is_exist(data)[0])

        data = {
            "username": 'testusername002',
            'email': 'testusername001@gmail.com',
            'password': "testpassword001",
            'confirmPassword': 'testpassword001'
        }
        self.assertEqual('This email has registered', self.user_rp.is_exist(data)[0])

        data = {
            "username": 'correct001',
            'email': 'correct001@gmail.com',
            'password': "correct001password",
            'confirmPassword': 'correct001password'
        }
        self.assertTrue(self.user_rp.is_exist(data) == [])

