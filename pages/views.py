from django.shortcuts import render
from django.views.generic.base import TemplateView
from ..projects.models import Project
from ..blog.models import Post

# Create your views here.

class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()[:3]
        context['blogs'] = Post.objects.all()[:3]
        return context

class AboutView(TemplateView):
    pass
