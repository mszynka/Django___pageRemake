from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=20, blank=False)
    logo = models.ImageField()
    link = models.URLField()

class User(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    mail = models.EmailField(blank=False)
    service = models.ManyToManyField(Service, through='ServiceManager', through_fields=('user','service'))

class Image(models.Model):
    name = models.CharField(max_length=40)
    caption = models.CharField(max_length=150)
    image = models.ImageField()

class Article(models.Model):
    title = models.CharField(max_length=100, blank=False)
    paragraphs = models.TextField()
    images = models.ManyToManyField(Image, through='ImageManager', through_fields=('article','image'))

class View(models.Model):
    name = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=150, blank=True)
    background_images = models.ManyToManyField(Image)
    articles = models.ManyToManyField(Article, through='ArticleManager', through_fields=('view','article'))

class ServiceManager(models.Model):
    user = models.ForeignKey(User)
    service = models.ForeignKey(Service)

class ArticleManager(models.Model):
    article = models.ForeignKey(Article)
    view = models.ForeignKey(View)

class ImageManager(models.Model):
    article = models.ForeignKey(Article)
    image = models.ForeignKey(Image)