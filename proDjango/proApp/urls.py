from django.urls import path
from . import views

urlpatterns = [
    path('', views.proAppFunction, name='proApp'),
    path('data/', views.proData, name='proData'),
    path('details/<int:item_id>', views.proDetail, name='item_detail'),
]
