from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator

# Create your views here.


def frontpage(request):

    # posts = Post.objects.all()

    # context = {
    #     'currentUser': username,
    #     'posts': posts
    # }

    return render(request, 'pages/front-page.html')


# def home(request, username):

#     posts = Post.objects.all()
#     paginate = Paginator(posts, 5)
#     page = request.GET.get('page')

#     context = {
#         'currentUser': username,
#         'posts': posts
#     }

#     return render(request, 'pages/home.html', context)

def home(request):

    posts = Post.objects.all()
    paginate = Paginator(posts, 5)
    page = request.GET.get('page')

    context = {
        # 'currentUser': username,
        'posts': posts
    }

    return render(request, 'pages/home.html', context)



def single(request, single):
    single = Post.objects.get(id=single)
    context = {
        'post': single
    }

    return render(request, 'pages/single.html', context)

def page(request, page):
    # page = Post.objects.get(id=page)
    context = {
        'page': about
    }

    return render(request, 'pages/single.html', context)

def about(request):
    # page = Post.objects.get(id=page)
    context = {
        'page': about
    }

    return render(request, 'pages/about.html', context)

def contact(request):
    # page = Post.objects.get(id=page)
    context = {
        'page': contact
    }

    return render(request, 'pages/contact.html', context)

def gallery(request):
    # page = Post.objects.get(id=page)
    context = {
        'page': gallery
    }

    return render(request, 'pages/gallery.html', context)

def portfolio(request):
    # page = Post.objects.get(id=page)
    context = {
        'page': portfolio
    }

    return render(request, 'pages/portfolio.html', context)

def services(request):
    # page = Post.objects.get(id=page)
    context = {
        'page': services
    }

    return render(request, 'pages/services.html', context)