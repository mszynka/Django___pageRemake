from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    mail = models.EmailField(blank=False)
    # services = models.ManyToManyField(Services) # (Foregin key Services) #git, linkedin TODO
    pass

class Service(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=20, blank=False)
    logo = models.ImageField()
    link = models.URLField()
    pass

class View(models.Model):
    name = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=150, blank=True)
    # background-images = TODO
    # articles = TODO
    pass

class Article(models.Model):
    title = models.CharField(max_length=100, blank=False)
    paragraphs = models.TextField()
    # images = TODO
    pass

class ServiceManager(models.Model):
    user = models.ForeignKey(User)
    service = models.ForeignKey(Service)
    # TODO many to many through
    pass

class ArticleManager(models.Model):
    # TODO many to many through
    pass

class ImageManager(models.Model):
    # TODO many to many through
    pass