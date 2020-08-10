from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    ordering = ['creation_date']