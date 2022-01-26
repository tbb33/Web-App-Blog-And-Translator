from re import template
from django.shortcuts import render

from blog.models import Post
from .models import Post

# Create your views here.

class BlogView:
    model = Post
    template_name = 'blog.html'