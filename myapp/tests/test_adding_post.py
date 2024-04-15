from django.test import TestCase, Client
from myapp.models import Post

class PostCreationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_post(self):
        response = self.client.post('/add_post/', {
            'title': 'Test Post',
            'body': 'This is a test post.'
        })

        self.assertEqual(response.status_code, 302)  # Assuming it redirects after successful creation

        # Check that the post was created in the database
        post = Post.objects.get(title='Test Post')
        self.assertEqual(post.body, 'This is a test post.')