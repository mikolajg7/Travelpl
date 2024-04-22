import requests
from django.test import TestCase

class JSONPlaceholderPostsContractTest(TestCase):
    def test_patch_posts_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        data = {
            'title': 'foo',
        }
        response = requests.patch(url, data=data)

        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check headers
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Check body structure
        post = response.json()
        self.assertEqual(post['title'], 'foo')  # JSONPlaceholder always returns the same input for PATCH requests