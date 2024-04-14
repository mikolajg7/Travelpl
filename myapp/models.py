from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
