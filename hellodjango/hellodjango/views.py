from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Home")


def hello(request):
    return HttpResponse("hello")


def add(request):
    print(request)
    sum = ""
    if request.GET:
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        sum = str(a + b)
    return HttpResponse("add" + sum)


def sub(request):
    print(request)
    sub = ""
    if request.GET:
        a = int(request.GET['a'])
        b = int(request.GET["b"])
        sub = str(a - b)
    return HttpResponse("sub" + sub)


def dict(request):
    d = {1: "Ashok", 2: "Adarsh"}
    name = ""
    if request.GET:
        rollno = int(request.GET["rollno"])
        name = d.get(rollno, "Not found")
    return HttpResponse(name)


def hospital(request):
    d = {1: "medical", 2: "opd", 3: "icu", 4: "general"}
    name = ""
    if request.GET:
        roomno = int(request.GET["roomno"])
        name = d.get(roomno, "not found")
    return HttpResponse(name)
