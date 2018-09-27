import unittest
from app import app
from flask import json


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        post_signup = dict(name="inception", username="Fahad", password="clooneyboss")
        response = self.app.post('/auth/signup', json=post_signup)
        self.assertIn("Fahad you have successfully created an account", str(response.data))

