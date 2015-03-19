from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# TODO make it work

def home(request):
    return HttpResponse("HOME")