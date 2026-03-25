from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post
from .forms import CommentForm

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    order_by = 'pub_date'

    def get_queryset(self, **kwargs):
        return super().get_queryset(**kwargs).filter(status=1)
    
#class PostDetailView(generic.DetailView):
#    model = Post
#    template_name = 'blog/post_detail.html'

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method=='post':
        form = CommentForm(request.Post)
        form.is_valid()
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment.user = request.user
        new_comment.save()
        return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post':post, 'form':form})