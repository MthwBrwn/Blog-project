from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogpage/home.html', context)

 
class PostListView(ListView):
    model = Post
    template_name = 'blogpage/home.html'
    context_object_name = 'posts'
    ordering = ['-date']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['tite', 'content']


def about(request):
    return render(request, 'blogpage/about.html', {'title': 'about'})