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
        post_login = dict(username="Inception", password="clooneyboss")
        response = self.app.post('/auth/login', json=post_login)
        self.assertIn("Inception you have logged created an account", str(response.data))
