from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Ensure User model is imported


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Add on_delete
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    slug = models.CharField(max_length=200, unique=True)
    categories = models.ForeignKey('blog.category', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('blog.category', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name