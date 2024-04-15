from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib import auth 

class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login(self):
        response = self.client.post('/login/', {
            'username': 'testuser',
            'passw': 'testpassword',
        })

        self.assertEqual(response.status_code, 302)  # Assuming it redirects after successful login

        # Check that the user was authenticated
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)