from django.shortcuts import render
from blog.models import Post, Category, Page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
# from .models import Article
# Create your views here.


def frontpage(request):

    # posts = Post.objects.all()

    # context = {
    #     'currentUser': username,
    #     'posts': posts
    # }

    return render(request, 'pages/front-page.html')

def home(request):

    post_list = Post.objects.all()
    paginate = Paginator(post_list, 6)
    
    page = request.GET.get('page')
    try:
        posts = paginate.page(page)
    except PageNotAnInteger:
        posts = paginate.page(1)
    except EmptyPage:
        posts = paginate.page(paginate.num_pages)
    
    context = {
        # 'currentUser': username,
        'posts': posts,
    }

    return render(request, 'pages/home.html', context)

def article_detail(request, slug):
    article = get_object_or_404(Post, slug=slug)
    context = {
        'post': article
    }
    return render(request, 'pages/single.html', context)

def page(request, single_page):
    page = Page.objects.get(slug=single_page)
    context = {
        'page': page
    }
    return render(request, 'pages/page.html', context)

def single(request, single):
    single = Post.objects.get(id=single)
    context = {
        'post': single
    }
    return render(request, 'pages/single.html', context)

def archive(request, category):
    cat = Category.objects.get(slug=category)
    post_list = Post.objects.filter(categories__pk=cat.id) # pk = primary key
    paginate = Paginator(post_list, 6)
    
    page = request.GET.get('page')
    categories = Category.get_all_categories()
    # categories = request.GET.get('category')
    try:
        posts = paginate.page(page)

    except PageNotAnInteger:
        posts = paginate.page(1)
    except EmptyPage:
        posts = paginate.page(paginate.num_pages)
    
    context = {
        # 'currentUser': username,
        'posts': posts,
        'categories': categories,
        'title': cat.title
    }

    return render(request, 'pages/archive.html', context)

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