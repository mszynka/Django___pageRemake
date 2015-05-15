from django.db import models
from ckeditor.fields import RichTextField
import datetime

class Service(models.Model):
    name = models.CharField(max_length=20, blank=False)
    logo = models.ImageField()
    link = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.name

class Userss(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    mail = models.EmailField(blank=False)

    def getName(self):
        return self.name + " " + self.surname

    def __str__(self):
        return self.name + " " + self.surname

class Image(models.Model):
    name = models.CharField(max_length=40)
    caption = models.CharField(max_length=150)
    image = models.ImageField()

    def __str__(self):
        return self.name

class View(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=150, blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    paragraphs = RichTextField()
    view = models.ForeignKey(View, default=1)
    date = models.DateField(auto_now_add=True, blank=True)
    posted = models.BooleanField(default=True)

    def __str__(self):
        return self.title