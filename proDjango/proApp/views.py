from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def proAppFunction(request):
    # return HttpResponse("Hello, World! This is the proApp function.")
    return render(request, 'proApp/pro.html')