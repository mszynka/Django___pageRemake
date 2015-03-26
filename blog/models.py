from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    text = models.TextField()
    date = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

class Category(models.Model):
    title
    slug