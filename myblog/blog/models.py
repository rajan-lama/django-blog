from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Ensure User model is imported


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Add on_delete
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
