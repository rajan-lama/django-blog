"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('username/<str:username>/', blog_views.home, name='username'),
    path('post/<int:single>/', blog_views.single, name='single'),
    path('about', blog_views.about),
    path('services', blog_views.services),
    path('portfolio', blog_views.portfolio),
    path('gallery', blog_views.gallery),
    path('blog', blog_views.home),
    path('contact', blog_views.contact),
    path('/<str:page>/', blog_views.page, name='page'),

    path("", blog_views.frontpage),
    # path("", blog_views.home),
]
