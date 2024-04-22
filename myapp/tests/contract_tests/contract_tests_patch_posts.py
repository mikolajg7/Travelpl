import requests
from django.test import TestCase

class JSONPlaceholderPostsContractTest(TestCase):
    def test_patch_posts_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        data = {
            'title': 'foo',
        }
        response = requests.patch(url, data=data)

        # Sprawdzenie kodu statusu
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie nagłówków
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Sprawdzenie struktury treści
        post = response.json()
        self.assertEqual(post['title'], 'foo')  # JSONPlaceholder zawsze zwraca tę samą wartość wejściową dla żądań PATCH
