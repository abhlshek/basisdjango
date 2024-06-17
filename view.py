from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Home")


def hello(request):
    return HttpResponse("hello")
