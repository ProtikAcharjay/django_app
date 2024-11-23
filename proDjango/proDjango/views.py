from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World! This is my first Django application.")

def test(request):
    test = "check"
    return HttpResponse(f"Hello, World! This is my first Django application. test: {test}")