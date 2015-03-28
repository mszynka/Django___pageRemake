from django.db import models
from django.db.models import permalink

class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    text = models.TextField()
    date = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')
    tags = models.ManyToManyField('blog.Tag')

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post',None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Tag(models.Model):
	title = models.CharField(max_length=70, unique=True)
	slug = models.SlugField(max_length=70, unique=True)

	def __str__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_tag', None, {'slug': self.slug})