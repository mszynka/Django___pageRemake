from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from simple_cms.models import Userss, View

def home(request):
    context = RequestContext(request)
    name = Userss.objects.all()[:1].get().name
    surname = Userss.objects.all()[:1].get().surname
    menu = View.objects.filter(enabled=True)

    values = {"username": name, "menu": menu}
    return render_to_response('index.html', values, context)
    #return HttpResponse("<html><body><h1>HOME</h1></body></html>")