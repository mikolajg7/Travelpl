import requests
from django.test import TestCase

class JSONPlaceholderPostsContractTest(TestCase):

    # Test kontraktu dla punktu końcowego POST /posts
    def test_post_posts_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        data = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        response = requests.post(url, data=data)

        # Sprawdzenie kodu statusu
        self.assertEqual(response.status_code, 201)

        # Sprawdzenie nagłówków
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Sprawdzenie struktury treści
        post = response.json()
        self.assertIn('id', post)
        self.assertEqual(post['id'], 101)  # JSONPlaceholder zawsze zwraca id równy 101 dla żądań POST
