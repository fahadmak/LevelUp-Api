import unittest
from app import app


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Tests for create user
    def test_create_user(self):
        post_signup = dict(name="inception", username="Fahad", password="clooneyboss")
        response = self.app.post('/auth/signup', json=post_signup)
        self.assertIn("Fahad you have successfully created an account", str(response.data))

    def test_create_user_empty_fields(self):
        post_signup = dict(name="inception", password="clooneyboss")
        response = self.app.post('/auth/signup', json=post_signup)
        self.assertIn("Please fill missing fields", str(response.data))

    def test_create_user_incorrect_input(self):
        post_signup = dict(name="inception", username=7, password="clooneyboss")
        response = self.app.post('/auth/signup', json=post_signup)
        self.assertIn("Please input correct information", str(response.data))

    # Tests for login user
    def test_login_user(self):
        post_login = dict(username='fahad3', password='pass123')
        response = self.app.post('/auth/login', json=post_login)
        self.assertIn("fahad3 you have logged in", str(response.data))

    def test_login_user_empty_fields(self):
        post_login = dict(username='fahad3')
        response = self.app.post('/auth/login', json=post_login)
        self.assertIn("Please fill missing fields", str(response.data))

    def test_login_user_incorrect_input(self):
        post_login = dict(username='fahad3', password=7)
        response = self.app.post('/auth/login', json=post_login)
        self.assertIn("Please input correct information", str(response.data))

    def test_login_user_password_do_not_match(self):
        post_login = dict(username='fahad3', password="1qwqee7")
        response = self.app.post('/auth/login', json=post_login)
        self.assertIn("Please input correct information", str(response.data))

    def test_login_user_already_logged_in(self):
        post_login1 = dict(username='fahad3', password='pass123')
        post_login2 = dict(username='fahad3', password='pass123')
        response1 = self.app.post('/auth/login', json=post_login1)
        response2 = self.app.post('/auth/login', json=post_login2)
        self.assertIn("You are already logged in", str(response2.data))
