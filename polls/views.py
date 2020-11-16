from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world")


def owner(request):
    return HttpResponse("Hello, world. 27d52bcb is the polls index.")