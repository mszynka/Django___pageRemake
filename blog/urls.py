from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.models import Post, Category, Tag, Comment

urlpatterns = patterns(
	'',
	url(r'^$', 'blog.views.index', name='view_blog'),
  url(r'^post/(?P<slug>[^\.]+)', 'blog.views.view_post',name='view_blog_post'),
  url(r'^categories/$', 'blog.views.view_categories', name='view_blog_categories'),
  url(r'^category/(?P<slug>[^\.]+)', 'blog.views.view_category',name='view_blog_category'),
  url(r'^tags/$', 'blog.views.view_tags', name='view_blog_tags'),
  url(r'^tag/(?P<slug>[^\.]+)', 'blog.views.view_tag', name='view_blog_tag'),
)