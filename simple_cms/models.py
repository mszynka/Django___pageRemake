from django.db import models
from ckeditor.fields import RichTextField
import datetime

class Service(models.Model):
    name = models.CharField(max_length=20, blank=False)
    logo = models.ImageField()
    link = models.URLField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    mail = models.EmailField(blank=False)

    def __str__(self):
        return self.name + " " + self.surname

class Image(models.Model):
    name = models.CharField(max_length=40)
    caption = models.CharField(max_length=150)
    image = models.ImageField()

    def __str__(self):
        return self.name

class View(models.Model):
    name = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100, blank=False)
    paragraphs = RichTextField()
    view = models.ForeignKey(View)
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title