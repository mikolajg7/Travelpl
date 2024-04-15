from django.test import TestCase, Client

class RegistrationPageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registration_page_opens_correctly(self):
        response = self.client.get('/registration/')  
        self.assertEqual(response.status_code, 200)