import requests
from django.test import TestCase

class JSONPlaceholderPostsContractTest(TestCase):

    # Contract test for the POST /posts endpoint
    def test_post_posts_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        data = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        response = requests.post(url, data=data)

        # Check status code
        self.assertEqual(response.status_code, 201)

        # Check headers
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Check body structure
        post = response.json()
        self.assertIn('id', post)
        self.assertEqual(post['id'], 101)  # JSONPlaceholder always returns an id of 101 for POST requests