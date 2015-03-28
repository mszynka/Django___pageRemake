from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from simple_cms.models import Userss, View, Service, Article

def page(request, specific):
	context = RequestContext(request)
	name = Userss.objects.all()[:1].get()
	menu = View.objects.filter(enabled=True)
	services = Service.objects.all()

	for item in menu:
		if item.name == specific:
			item.open = True
			articles = Article.objects.filter(view=item)

	return render_to_response('index.html',
                              {"name": name, "menu": menu, "articles": articles},
                              context)