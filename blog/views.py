from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Ola Ade',
        'title': 'Blog post 1',
        'content': 'First post',
        'date_posted': 'August 27, 2020'
    },

    {
        'author': 'Sandr Ade',
        'title': 'Blog post 2',
        'content': 'Second post',
        'date_posted': 'August 28, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})