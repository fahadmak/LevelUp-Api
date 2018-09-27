import unittest
from app import app
from flask import json


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

