from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
