import requests
from django.test import TestCase

class JSONPlaceholderPhotosContractTest(TestCase):

    # Test kontraktu dla punktu końcowego /photos
    def test_photos_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/photos'
        response = requests.get(url)

        # Sprawdzenie kodu statusu
        self.assertEqual(response.status_code, 200)

        # Sprawdzenie nagłówków
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Sprawdzenie struktury treści
        photos = response.json()
        for photo in photos:
            self.assertIn('albumId', photo)
            self.assertIn('id', photo)
            self.assertIn('title', photo)
            self.assertIn('url', photo)
            self.assertIn('thumbnailUrl', photo)
