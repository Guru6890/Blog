from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    order_by = 'pub_date'

    def get_queryset(self, **kwargs):
        return super().get_queryset(**kwargs).filter(status=1)
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'