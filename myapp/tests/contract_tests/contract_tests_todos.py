import requests
from django.test import TestCase

class JSONPlaceholderTodosContractTest(TestCase):

    # Contract test for the /todos endpoint
    def test_todos_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/todos'
        response = requests.get(url)

        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check headers
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Check body structure
        todos = response.json()
        for todo in todos:
            self.assertIn('userId', todo)
            self.assertIn('id', todo)
            self.assertIn('title', todo)
            self.assertIn('completed', todo)