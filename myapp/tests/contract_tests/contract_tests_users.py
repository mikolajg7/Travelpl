import requests
from django.test import TestCase

class JSONPlaceholderUsersContractTest(TestCase):

    # Contract test for the /users endpoint
    def test_users_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)

        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check headers
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Check body structure
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