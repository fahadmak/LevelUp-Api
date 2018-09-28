import unittest
from app import app


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Tests for create task
    def test_create_task(self):
        post_signup = dict(task_name="inception")
        response = self.app.post('/task/1', json=post_signup)
        self.assertIn("inception task has been created", str(response.data))

    def test_create_task_empty_fields(self):
        post_signup = dict()
        response = self.app.post('/task/1', json=post_signup)
        self.assertIn("Please fill in task name", str(response.data))

