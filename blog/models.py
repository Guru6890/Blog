from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

#class PostManager(models.Manager):
#    def get_queryset(self):
#        return super().get_queryset().filter(status=1)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    STATUS_CHOICES = [(0, 'Draft'), (1, 'Published')]
    
    status = models.IntegerField(choices=STATUS_CHOICES)

    #objects = models.Manager()
    #postfilter = PostManager()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        if((update_fields := kwargs.get(update_fields)) is not None and 'title' in update_fields):
            kwargs[update_fields] = set(update_fields) | {'slug'}

        super().save(**kwargs)

    #class Meta:
    #    ordering = ['-pub_date']

class Category(models.Model):
    name = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True,
                               related_name='replies'
                               )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
