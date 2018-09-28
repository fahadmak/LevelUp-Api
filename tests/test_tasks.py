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
        post_task1 = dict(task_name="fahad")
        response2 = self.app.post('/task/1', json=post_task1)
        response3 = self.app.delete('/task/1/delete/1')
        self.assertIn("fahad task has been deleted", str(response3.data))

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

    # Tests for delete all tasks
    def test_delete_all_tasks(self):
        post_login = dict(username='fahad3', password='pass123')
        response = self.app.post('/auth/login', json=post_login)
        post_task1 = dict(task_name="inceptions")
        response2 = self.app.post('/task/1', json=post_task1)
        response3 = self.app.delete('/task/1/delete')
        self.assertIn("All tasks have been successfully deleted", str(response3.data))

    def test_delete_all_tasks_no_tasks(self):
        post_login = dict(username='Andela', password='pass12345')
        response = self.app.post('/auth/login', json=post_login)
        response3 = self.app.delete('/task/6/delete')
        self.assertIn("You have no tasks", str(response3.data))

    # Tests for recover deleted tasks
    def test_recover_deleted_tasks(self):
        post_login = dict(username='fahad3', password='pass123')
        response = self.app.post('/auth/login', json=post_login)
        post_task1 = dict(task_name="fahad")
        response2 = self.app.post('/task/1', json=post_task1)
        response3 = self.app.delete('/task/1/delete/3')
        response4 = self.app.get('/task/1/delete/1/recover')
        self.assertIn("fahad has been recovered successfully", str(response4.data))

    def test_recover_deleted_tasks_no_tasks(self):
        post_login = dict(username='phillipwere', password='pass12345')
        response = self.app.post('/auth/login', json=post_login)
        response3 = self.app.delete('/task/4/delete')
        response4 = self.app.get('/task/4/delete/1/recover')
        self.assertIn("Task does not exist", str(response4.data))

    # Tests for marked tasks
    def test_mark_task(self):
        post_login = dict(username='fahad3', password='pass123')
        response = self.app.post('/auth/login', json=post_login)
        post_task3 = dict(marked="True")
        response3 = self.app.put('/task/1/mark/2', json=post_task3)
        self.assertIn("True has been recovered successfully", str(response3.data))

    # Tests for marked tasks
    def test_mark_task_empty(self):
        post_login = dict(username='phillipwere', password='pass12345')
        response = self.app.post('/auth/login', json=post_login)
        post_task3 = dict()
        response3 = self.app.put('/task/4/mark/3', json=post_task3)
        self.assertIn("Please fill in task name", str(response3.data))




