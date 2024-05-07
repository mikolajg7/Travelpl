from django.test import TestCase, Client

class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_opens_correctly(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)