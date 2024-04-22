import requests
from django.test import TestCase

class JSONPlaceholderAlbumsContractTest(TestCase):

    # Contract test for the /albums endpoint
    def test_albums_endpoint(self):
        url = 'https://jsonplaceholder.typicode.com/albums'
        response = requests.get(url)

        # Check status code
        self.assertEqual(response.status_code, 200)

        # Check headers
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=utf-8')

        # Check body structure
        albums = response.json()
        for album in albums:
            self.assertIn('userId', album)
            self.assertIn('id', album)
            self.assertIn('title', album)