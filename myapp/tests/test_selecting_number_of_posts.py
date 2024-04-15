from django.test import TestCase, Client
from myapp.models import Post

class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_post_count(self):
        response = self.client.get('', {'post_count': 5})

        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct number of posts is included in the response context
        self.assertEqual(len(response.context['posts']), 5)