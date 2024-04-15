from django.test import TestCase, Client

class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_logout_view(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/')