from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    git_hub = models.URLField()
    git_live = models.URLField(null=True, blank=True)
    #image = models.ImageField()