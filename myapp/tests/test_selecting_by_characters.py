from django.test import TestCase, Client

class Home2ViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home2_view(self):
        response = self.client.get('/home2/')
        self.assertEqual(response.status_code, 200)