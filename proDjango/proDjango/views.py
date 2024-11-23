from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, World! This is my first Django application.")

def test(request):
    test = "check"
    return HttpResponse(f"Hello, World! This is my first Django application. test: {test}")

def templateReturn(request):
    temp = "yes it's working!"
    return render(request, 'app1/temp.html', {'temp': temp})