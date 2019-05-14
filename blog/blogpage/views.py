from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Matthew',
        'title': 'first post',
        'content': 'This is the very first post.',
        'date': 'dummy date'
    },

    {
        'author': 'Matthew II',
        'title': 'second post',
        'content': 'This is yet another post.',
        'date': 'dummy date II'
    }


]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogpage/home.html', context)


def about(request):
    return render(request, 'blogpage/about.html', {'title': 'about'})