import requests
from django.test import TestCase

class JSONPlaceholderTodosContractTest(TestCase):

    # Test kontraktu dla punktu końcowego /todos
    def test_todos_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/todos'
        response = requests.get(url)

        # Sprawdzenie kodu statusu
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie nagłówków
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Sprawdzenie struktury treści
        todos = response.json()
        for todo in todos:
            self.assertIn('userId', todo)
            self.assertIn('id', todo)
            self.assertIn('title', todo)
            self.assertIn('completed', todo)
