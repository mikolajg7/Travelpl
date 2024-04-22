import requests
from django.test import TestCase

class JSONPlaceholderUsersContractTest(TestCase):

    # Test kontraktu dla punktu końcowego /users
    def test_users_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)

        # Sprawdzenie kodu statusu
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie nagłówków
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Sprawdzenie struktury treści
        users = response.json()
        for user in users:
            self.assertIn('id', user)
            self.assertIn('name', user)
            self.assertIn('username', user)
            self.assertIn('email', user)
            self.assertIn('address', user)
            self.assertIn('phone', user)
            self.assertIn('website', user)
            self.assertIn('company', user)
