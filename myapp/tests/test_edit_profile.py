from django.test import TestCase, Client
from django.contrib.auth.models import User  # Add this line

class AccountOptionsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_edit_profile(self):
        response = self.client.post('/accountOptions/', {
            'username': 'testuser',
            'email': 'test@email',
            'pass1': 'testpassword',
            'pass2': 'testpassword',
        })

        self.assertEqual(response.status_code, 302)  

        # Check that the user was created in the database
        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user)