import requests
from django.test import TestCase

class JSONPlaceholderContractTest(TestCase):

    # Test kontraktu dla punktu końcowego /comments
    def test_comments_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/comments'
        response = requests.get(url)

        # Sprawdzenie kodu statusu
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie nagłówków
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Sprawdzenie struktury treści
        comments = response.json()
        for comment in comments:
            self.assertIn('postId', comment)
            self.assertIn('id', comment)
            self.assertIn('name', comment)
            self.assertIn('email', comment)
            self.assertIn('body', comment)
