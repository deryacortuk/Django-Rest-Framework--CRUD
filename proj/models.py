from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
