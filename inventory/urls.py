from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_items, name='inventoryitems'),
    path('<int:inventoryitem_id>/', views.inventory_detail, name='inventory_detail'),
    path('add/', views.add_item, name='add_item'),
]