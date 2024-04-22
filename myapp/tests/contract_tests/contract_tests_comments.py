import requests
from django.test import TestCase

class JSONPlaceholderContractTest(TestCase):

    # Contract test for the /comments endpoint
    def test_comments_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/comments'
        response = requests.get(url)

        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check headers
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Check body structure
        comments = response.json()
        for comment in comments:
            self.assertIn('postId', comment)
            self.assertIn('id', comment)
            self.assertIn('name', comment)
            self.assertIn('email', comment)
            self.assertIn('body', comment)