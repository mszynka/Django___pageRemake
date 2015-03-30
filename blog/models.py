from django.db import models
from django.db.models import permalink

class BlogSettings(models.Model):
	attribute = models.CharField(max_length=100, unique=True)
	value = models.CharField(max_length=150, default="0")

	class Meta:
		verbose_name = "Attribute"
		verbose_name_plural = "Settings"

class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    text = models.TextField()
    date = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')
    tags = models.ManyToManyField('blog.Tag')
    posted = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post',None, { 'slug': self.slug })

    class Meta:
	    verbose_name_plural = "  Posts"

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

    class Meta:
	    verbose_name_plural = " > Categories"

class Tag(models.Model):
	title = models.CharField(max_length=70, unique=True)
	slug = models.SlugField(max_length=70, unique=True)

	def __str__(self):
		return '%s' % self.slug

	class Meta:
		verbose_name_plural = " > Tags"

	@permalink
	def get_absolute_url(self):
		return ('view_blog_tag', None, {'slug': self.slug})

class Comment:
	date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max__length=100,blank=False)
	email = models.EmailField()
	website = models.URLField()
	text = models.TextField
	replies = models.ManyToManyField(blog.Comment)
	parent = models.ForeignKey(blog.Comment)
	post = models.ForeignKey(blog.post)

	def __str__(self):
		return self.text[0:30] #returns first n characters

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'