from django.test import TestCase, Client
from django.contrib.auth.models import User

class RegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registration(self):
        response = self.client.post('/registration/', {
            'username': 'testuser',
            'email': 'test@email',
            'pass1': 'testpassword',
            'pass2': 'testpassword',
        })

        self.assertEqual(response.status_code, 302)  # Assuming it redirects after successful registration

        # Check that the user was created in the database
        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user)