import requests
from django.test import TestCase

class JSONPlaceholderPostsContractTest(TestCase):
    def test_delete_posts_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        response = requests.delete(url)

        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check headers
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Check body structure
        self.assertEqual(response.text, '{}')  # JSONPlaceholder always returns an empty body for DELETE requests