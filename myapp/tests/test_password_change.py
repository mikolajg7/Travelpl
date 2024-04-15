from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate

class PasswordChangeTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='oldpassword')

    def test_password_change(self):
        self.client.login(username='testuser', password='oldpassword')

        response = self.client.post(reverse('/accountOptions/'), {  
            'pass2': 'newpassword',
        })

        self.assertEqual(response.status_code, 302)

        self.test_user.refresh_from_db()
        self.assertTrue(self.test_user.check_password('newpassword'))