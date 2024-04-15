from django.test import TestCase, Client

class LoginPageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_page_opens_correctly(self):
        response = self.client.get('/login/') 
        self.assertEqual(response.status_code, 200)