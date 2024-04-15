from django.test import TestCase, Client
from django.contrib.auth.models import User

class ProfilePageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

    def test_profile_page_opens_correctly(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/accountOptions/')  
        self.assertEqual(response.status_code, 200)