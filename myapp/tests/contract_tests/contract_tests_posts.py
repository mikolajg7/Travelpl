import requests
from django.test import TestCase

class JSONPlaceholderContractTest(TestCase):

    # Contract test for the /posts endpoint
    def test_posts_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(url)

        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check headers
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Check body structure
        posts = response.json()
        for post in posts:
            self.assertIn('userId', post)
            self.assertIn('id', post)
            self.assertIn('title', post)
            self.assertIn('body', post)