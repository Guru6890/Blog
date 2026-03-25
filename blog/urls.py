from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.PostListView.as_view(), name='home'),
    path('post/<slug:slug/>', views.PostDetailView.as_view(), name='post'),
]