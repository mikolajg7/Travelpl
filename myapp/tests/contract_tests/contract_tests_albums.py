import requests
from django.test import TestCase

class JSONPlaceholderAlbumsContractTest(TestCase):

    # Test kontraktu dla punktu końcowego /albums
    def test_albums_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/albums'
        response = requests.get(url)

        # Sprawdzenie kodu statusu
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie nagłówków
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Sprawdzenie struktury treści
        albums = response.json()
        for album in albums:
            self.assertIn('userId', album)
            self.assertIn('id', album)
            self.assertIn('title', album)
