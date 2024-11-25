from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ProItems
# Create your views here.
def proAppFunction(request):
    # return HttpResponse("Hello, World! This is the proApp function.")
    return render(request, 'proApp/pro.html')

def proData(request):
    pro_items = ProItems.objects.all()
    return render(request, 'proApp/prodata.html', {'pro_items': pro_items})

def proDetail(request, item_id):
    pro_item = get_object_or_404(ProItems, id=item_id)
    return render(request, 'proApp/prodetails.html', {'pro_item': pro_item})
