from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Ensure User model is imported
from django.template.defaultfilters import slugify
from django.utils.text import slugify
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Add on_delete
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, unique=True)
    # slug = models.CharField(max_length=200, unique=True, default=slugify(unidecode(title)))
    categories = models.ManyToManyField('blog.category',null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    # This ensures that if no slug is provided, it is auto-generated from the title.
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('blog.category', on_delete=models.CASCADE, null=True, blank=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    # This ensures that if no slug is provided, it is auto-generated from the title.
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, unique=True)
    
    # This ensures that if no slug is provided, it is auto-generated from the title.
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title