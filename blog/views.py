from blog.models import Post, Category, Tag, BlogSettings, Comment, Reply
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
from django.db.models import Q

def index(request):
	posts = Post.objects.filter(posted=True)
	posts_per_page = BlogSettings.objects.filter(attribute='posts-per-page').order_by('-date').get().value
	paginator = Paginator(posts,posts_per_page)

	page = request.GET.get('page')
	try:
		posts_on_page = paginator.page(page)
	except PageNotAnInteger:
		posts_on_page = paginator.page(1)
	except EmptyPage:
		posts_on_page = paginator.page(paginator.num_pages)

	for post in posts_on_page:
		post.tagsxy = list()
		for tag in post.tags.all():
			post.tagsxy.append(tag)

	return render_to_response('blog.html', {
		'nav_home': True,
		'categories': Category.objects.all(),
	    'tags': Tag.objects.all(),
	  'posts': posts_on_page,
	  'welcome_message': BlogSettings.objects.filter(attribute='welcome-message').get().value,
	  'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def view_post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	comments = Comment.objects.filter(post=post)

	for comment in comments:
		comment.replies = Reply.objects.filter(parent=comment)

	ains = Post.objects.filter(category=post.category)[:5]
	ain = list()

	for a in ains:
		if a.pk != post.pk:
			ain.append(a)

	return render_to_response('view_post.html', {
		'post': post,
	    'comments' : comments,
	    'also_in_cat': ain,
	    'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	posts = Post.objects.filter(category=category, posted=True)
	posts_per_page = BlogSettings.objects.filter(attribute='posts-per-page').order_by('-date').get().value
	paginator = Paginator(posts,posts_per_page)

	page = request.GET.get('page')
	try:
		posts_on_page = paginator.page(page)
	except PageNotAnInteger:
		posts_on_page = paginator.page(1)
	except EmptyPage:
		posts_on_page = paginator.page(paginator.num_pages)

	return render_to_response('view_category.html', {
		'category': category,
		'nav_cat': True,
		'posts': posts_on_page,
	    'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def view_categories(request):
	categories = Category.objects.all()
	for category in categories:
		category.post_count = Post.objects.filter(category=category,posted=True).count()
	return render_to_response('view_categories.html', {
		'nav_cat': True,
		'categories': categories,
	    'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def view_tag(request,slug):
	tag = get_object_or_404(Tag, slug=slug)
	posts = Post.objects.filter(tags=tag, posted=True)
	posts_per_page = BlogSettings.objects.filter(attribute='posts-per-page').order_by('-date').get().value
	paginator = Paginator(posts,posts_per_page)

	page = request.GET.get('page')
	try:
		posts_on_page = paginator.page(page)
	except PageNotAnInteger:
		posts_on_page = paginator.page(1)
	except EmptyPage:
		posts_on_page = paginator.page(paginator.num_pages)

	return render_to_response('view_tag.html', {
		'tag': tag,
		'nav_tags': True,
	    'posts': posts_on_page,
	    'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def view_tags(request):
	tags = Tag.objects.all()
	for tag in tags:
		tag.post_count = Post.objects.filter(tags=tag,posted=True).count()
	return render_to_response('view_tags.html', {
		'nav_tags': True,
		'tags': tags,
	    'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def new_comment(request, name, email, website, text, post):
	pass