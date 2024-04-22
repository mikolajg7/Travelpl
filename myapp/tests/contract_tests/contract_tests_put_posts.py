import requests
from django.test import TestCase

class JSONPlaceholderPostsContractTest(TestCase):
    def test_put_posts_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        data = {
            'id': 1,
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        response = requests.put(url, data=data)

        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check headers
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Check body structure
        post = response.json()
        post['userId'] = int(post['userId'])  # Convert userId to integer
        self.assertEqual(post, data)  # JSONPlaceholder always returns the same input for PUT requests