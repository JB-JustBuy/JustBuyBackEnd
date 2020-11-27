from src.repository.user_respository import UserRepository
import unittest


class TestUserRepository(unittest.TestCase):
    def test_validate_email(self):
        email = "efaina"
        try:
            UserRepository.validate_email(email)
        except ValueError as e:
            self.assertEqual("email format error", e.args[0])

    def test_validate_password(self):
        password = "tset"
        try:
            UserRepository.validate_password(password)
        except ValueError as e:
            self.assertEqual("length of password needs to bigger than 8", e.args[0])
