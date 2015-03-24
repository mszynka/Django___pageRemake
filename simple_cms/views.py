from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.template import RequestContext

# TODO make it work

def home(request):
    data = RequestContext(request, {'data':'is it?',})
    return render_to_response('index.html', data)
    #return HttpResponse("<html><body><h1>HOME</h1></body></html>")