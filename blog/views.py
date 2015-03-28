from blog.models import Post, Category, Tag, BlogSettings
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	posts = Post.objects.all()
	posts_per_page = BlogSettings.objects.filter(attribute='posts-per-page').get().value
	paginator = Paginator(posts,posts_per_page)

	page = request.GET.get('page')
	try:
		posts_on_page = paginator.page(page)
	except PageNotAnInteger:
		posts_on_page = paginator.page(1)
	except EmptyPage:
		posts_on_page = paginator.page(paginator.num_pages)

	return render_to_response('blog.html', {
		'nav_home': True,
		'categories': Category.objects.all(),
	    'tags': Tag.objects.all(),
	  'posts': posts_on_page,
	  'welcome_message': BlogSettings.objects.filter(attribute='welcome-message').get().value,
	  'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def view_post(request, slug):
	return render_to_response('view_post.html', {
		'post': get_object_or_404(Post, slug=slug),
	    'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	posts = Post.objects.filter(category=category)
	posts_per_page = BlogSettings.objects.filter(attribute='posts-per-page').get().value
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
		'posts': posts_on_page,
	    'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def view_categories(request):
	categories = Category.objects.all()
	for category in categories:
		category.post_count = Post.objects.filter(category=category).count()
	return render_to_response('view_categories.html', {
		'nav_cat': True,
		'categories': categories,
	    'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def view_tag(request,slug):
	tag = get_object_or_404(Tag, slug=slug)
	posts = Post.objects.filter(tags=tag)
	posts_per_page = BlogSettings.objects.filter(attribute='posts-per-page').get().value
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
	    'posts': posts_on_page,
	    'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})

def view_tags(request):
	tags = Tag.objects.all()
	for tag in tags:
		tag.post_count = Post.objects.filter(tags=tag).count()
	return render_to_response('view_tags.html', {
		'nav_tags': True,
		'tags': tags,
	    'blog_title': BlogSettings.objects.filter(attribute='blog-title').get().value
	})