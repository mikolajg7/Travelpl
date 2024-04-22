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

        # Sprawdzenie kodu statusu
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie nagłówków
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Sprawdzenie struktury treści
        post = response.json()
        post['userId'] = int(post['userId'])  # Konwersja userId na liczbę całkowitą
        self.assertEqual(post, data)  # JSONPlaceholder zawsze zwraca ten sam input dla żądań PUT
