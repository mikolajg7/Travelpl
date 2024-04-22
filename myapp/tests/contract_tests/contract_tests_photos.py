import requests
from django.test import TestCase

class JSONPlaceholderPhotosContractTest(TestCase):

    # Contract test for the /photos endpoint
    def test_photos_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/photos'
        response = requests.get(url)

        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check headers
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Check body structure
        photos = response.json()
        for photo in photos:
            self.assertIn('albumId', photo)
            self.assertIn('id', photo)
            self.assertIn('title', photo)
            self.assertIn('url', photo)
            self.assertIn('thumbnailUrl', photo)