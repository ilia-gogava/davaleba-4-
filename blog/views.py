from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.views.generic import ListView, DetailView # new


class BlogListView(ListView):
    model = Pos
    template_name = "home.html"

class BlogDetailView(DetailView): # new
    model = Post
    template_name = "post_detail.html"

# Create your views here.

