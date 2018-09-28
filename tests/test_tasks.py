import unittest
from app import app


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Tests for create task
    def test_create_task(self):
        post_login = dict(username='fahad3', password='pass123')
        response = self.app.post('/auth/login', json=post_login)
        post_task = dict(task_name="inception")
        response = self.app.post('/task/1', json=post_task)
        self.assertIn("inception task has been created", str(response.data))

    def test_create_task_empty_fields(self):
        post_login = dict(username='fahad3', password='pass123')
        response = self.app.post('/auth/login', json=post_login)
        post_task = dict()
        response = self.app.post('/task/1', json=post_task)
        self.assertIn("Please fill in task name", str(response.data))

    def test_create_task_incorrect_input(self):
        post_login = dict(username='fahad3', password='pass123')
        response = self.app.post('/auth/login', json=post_login)
        post_task = dict(task_name=1234)
        response = self.app.post('/task/1', json=post_task)
        self.assertIn("Task name should be in alphabetical characters", str(response.data))

    def test_create_task_if_user_not_logged_in(self):
        post_task = dict(task_name=1234)
        response = self.app.post('/task/2', json=post_task)
        self.assertIn("Task name should be in alphabetical characters", str(response.data))

    def test_create_task_if_already_exists(self):
        post_login = dict(username='minatti', password='pass1233')
        response = self.app.post('/auth/login', json=post_login)
        post_task1 = dict(task_name="inception")
        response3 = self.app.post('/task/2', json=post_task1)
        post_task2 = dict(task_name="inception")
        response2 = self.app.post('/task/2', json=post_task2)
        self.assertIn("Task name already exists", str(response2.data))

    # Tests for delete task
    def test_delete_task(self):
        post_login = dict(username='fahad3', password='pass123')
        response = self.app.post('/auth/login', json=post_login)
        post_task1 = dict(task_name="inception")
        response2 = self.app.post('/task/1', json=post_task1)
        response3 = self.app.delete('/task/1/delete/1')
        self.assertIn("inception task has been deleted", str(response3.data))

    def test_delete_task_user_not_logged_in(self):
        post_task1 = dict(task_name="inceptions")
        response2 = self.app.post('/task/2', json=post_task1)
        response3 = self.app.delete('/task/3/delete/2')
        self.assertIn("Please Login before you can access the account", str(response3.data))

    def test_delete_task_task_doesnot_exist(self):
        post_login = dict(username='fahad3', password='pass123')
        response = self.app.post('/auth/login', json=post_login)
        response3 = self.app.delete('/task/1/delete/1')
        self.assertIn("Task does not exist", str(response3.data))

