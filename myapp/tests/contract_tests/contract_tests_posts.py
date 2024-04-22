import requests
from django.test import TestCase

class JSONPlaceholderContractTest(TestCase):

    # Test kontraktu dla punktu końcowego /posts
    def test_posts_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(url)

        # Sprawdzenie kodu statusu
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie nagłówków
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Sprawdzenie struktury treści
        posts = response.json()
        for post in posts:
            self.assertIn('userId', post)
            self.assertIn('id', post)
            self.assertIn('title', post)
            self.assertIn('body', post)
