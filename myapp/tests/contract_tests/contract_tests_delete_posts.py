import requests
from django.test import TestCase

class JSONPlaceholderPostsContractTest(TestCase):
    def test_delete_posts_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        response = requests.delete(url)

        # Sprawdzenie kodu statusu
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie nagłówków
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Sprawdzenie struktury treści
        self.assertEqual(response.text, '{}')  # JSONPlaceholder zawsze zwraca pusty body dla żądań DELETE
