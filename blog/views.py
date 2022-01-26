from re import template
from django.shortcuts import render
from django.views import generic

from blog.models import Post
from .models import Post

# Create your views here.

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'