from django.contrib import admin
from .models import Post, Category, Page

# Register your models here.
# admin.site.register(Post)

# This automatically fills the slug field in the Django admin panel.
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, ArticleAdmin)

admin.site.register(Category, ArticleAdmin)

admin.site.register(Page, ArticleAdmin)